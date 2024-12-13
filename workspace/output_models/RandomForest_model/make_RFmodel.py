import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error
import joblib
from sklearn.preprocessing import LabelEncoder
import time
import numpy as np

# CSVデータの読み込み
data = pd.read_csv("format_data.csv")

# DataFrameの作成
df1 = pd.DataFrame(data)
df1 = df1[["Kinryou","Time","Ninki",
"Race Number","Distance","Weight","Weight Change",
"Ground_ダ","Ground_芝","Ground_障","Condition_不",
"Condition_稍","Condition_良","Condition_重","Weather_小雨",
"Weather_小雪","Weather_晴","Weather_曇","Weather_雨","Weather_雪","Sex","Age"]]
df1 = df1.dropna()

# 特徴量とターゲット変数の定義
X = df1.drop('Time', axis=1)
y = df1['Time']

X = X.apply(pd.to_numeric, errors='coerce').astype(np.float64)
y = y.apply(pd.to_numeric, errors='coerce').astype(np.float64)

# データを訓練データとテストデータに分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# ランダムフォレスト回帰モデルを構築
model = RandomForestRegressor(n_estimators=100, random_state=0)

print("start fitting")

start = time.time()  # 現在時刻（処理開始前）を取得

# モデルを訓練
model.fit(X_train, y_train)

end = time.time()  # 現在時刻（処理完了後）を取得
time_diff = end - start  # 処理完了後の時刻から処理開始前の時刻を減算する
print(time_diff)  # 処理にかかった時間データを使用

# モデルの性能評価
y_pred = model.predict(X_train)
mse = mean_squared_error(y_pred, y_train)
print(f"Mean Squared Error(Train): {mse}")

y_pred = model.predict(X_test)
mse = mean_squared_error(y_pred, y_test)
print(f"Mean Squared Error(Test): {mse}")

# モデルを保存
model_file_path = "random_forest_model.pkl"
joblib.dump(model, model_file_path)
print(f"Model saved to {model_file_path}")
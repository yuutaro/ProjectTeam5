import pandas as pd
import xgboost as xgb
import numpy as np

# 1. データの読み込み
data = pd.read_csv("../../team2/data/format_data.csv")

# 2. 特徴量とターゲットの設定
df = pd.DataFrame(data)
df = df[["Kinryou","Time_x","Ninki",
"Race Number","Distance","Weight","Weight Change",
"Ground_ダ","Ground_芝","Ground_障","Condition_不",
"Condition_稍","Condition_良","Condition_重","Weather_小雨",
"Weather_小雪","Weather_晴","Weather_曇","Weather_雨","Weather_雪","Sex","Age"]]
df = df.dropna()

X = df.drop('Time_x', axis=1)
y = df['Time_x']

X = X.apply(pd.to_numeric, errors='coerce').astype(np.float64)
y = y.apply(pd.to_numeric, errors='coerce').astype(np.float64)

# 3. XGBoostモデルの構築
xgb_model = xgb.XGBRegressor(
    n_estimators=50,       # ツリーの本数
    learning_rate=0.1,     # 学習率
    max_depth=5,           # ツリーの深さ
    random_state=0,
)

# 4. モデルのトレーニング
xgb_model.fit(X, y)

# 5. モデルをファイルとして保存
xgb_model.save_model("xgb_model.json")
print("モデルを保存しました: xgb_model.json")

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error
import joblib
from sklearn.preprocessing import LabelEncoder
import time

# CSVファイルを読み込み
file_path = "/home/user/dev/ProjectTeam5/workspace/team1/notebook/data-074/format_data.csv"
df = pd.read_csv(file_path)

# 欠損値を削除
df = df.dropna()

# 説明変数 (features) と目的変数 (target) に分ける
target_column = "Time"
X = df.drop(columns=[target_column])
y = df[target_column]

# 数値型でない列を文字列型に変換してエンコード
for col in X.select_dtypes(include='object').columns:
    X[col] = X[col].astype(str)  # データ型を統一
    le = LabelEncoder()
    X[col] = le.fit_transform(X[col])

# メモリ効率化
def reduce_memory_usage(df):
    for col in df.columns:
        col_type = df[col].dtype
        if col_type != object:
            c_min = df[col].min()
            c_max = df[col].max()
            if str(col_type)[:3] == 'int':
                if c_min > -128 and c_max < 127:
                    df[col] = df[col].astype('int8')
                elif c_min > -32768 and c_max < 32767:
                    df[col] = df[col].astype('int16')
                elif c_min > -2147483648 and c_max < 2147483647:
                    df[col] = df[col].astype('int32')
            elif str(col_type)[:5] == 'float':
                df[col] = df[col].astype('float32')
    return df

X = reduce_memory_usage(X)

# データを訓練データとテストデータに分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# ランダムフォレスト回帰モデルを構築
model = RandomForestRegressor(n_estimators=100, random_state=0)

start = time.time()  # 現在時刻（処理開始前）を取得

# モデルを訓練
model.fit(X_train, y_train)

end = time.time()  # 現在時刻（処理完了後）を取得
time_diff = end - start  # 処理完了後の時刻から処理開始前の時刻を減算する
print(time_diff)  # 処理にかかった時間データを使用

# テストデータで予測
y_pred = model.predict(X_test)

# モデルの性能評価
mse = mean_squared_error(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)
print(f"Mean Squared Error: {mse}")
print(f"Mean Absolute Error: {mae}")

# モデルを保存
model_file_path = "/home/user/dev/ProjectTeam5/workspace/team1/notebook/data-074/random_forest_model.pkl"
joblib.dump(model, model_file_path)
print(f"Model saved to {model_file_path}")
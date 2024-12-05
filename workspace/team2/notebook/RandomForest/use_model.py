import pandas as pd
from sklearn.model_selection import train_test_split
import joblib
from sklearn.preprocessing import LabelEncoder

# CSVファイルを読み込み（メモリ効率化のオプションを追加）
file_path = "/home/user/dev/ProjectTeam5/workspace/team1/notebook/data-074/format_data.csv"
df = pd.read_csv(file_path, low_memory=False)

# 欠損値を削除
df = df.dropna()

# 必要な列だけ選択（不要な列をスキップ）
usecols = df.columns  # 必要に応じてカラム名を絞り込む
df = df[usecols]

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

# モデルの読み込み
model_file_path = "/home/user/dev/ProjectTeam5/workspace/team1/notebook/data-074/random_forest_model.pkl"
loaded_model = joblib.load(model_file_path)

# 新しいデータで予測
new_data = X_test.iloc[:5]  # 例としてテストデータの最初の5行を使用
predictions = loaded_model.predict(new_data)
print(f"Predictions: {predictions}")
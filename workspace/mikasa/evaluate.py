import tensorflow as tf
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

#  データの読み込み（学習時と同じ前処理を行う）
merged_table = pd.read_csv('./data/merged_table_finished3.csv')
merged_table = merged_table.drop(['Date', 'Code'], axis=1)

# LabelEncoderのインスタンスを生成（必須）
le_jockey = LabelEncoder()
le_trainer = LabelEncoder()
le_horsename = LabelEncoder()

# fitを実行（必須）
le_jockey.fit(merged_table['Jockey'])
le_trainer.fit(merged_table['Trainer'])
le_horsename.fit(merged_table['Horse Name'])

# transformを実行
merged_table["Jockey"] = le_jockey.transform(merged_table["Jockey"])
merged_table["Trainer"] = le_trainer.transform(merged_table["Trainer"])
merged_table["Horse Name"] = le_horsename.transform(merged_table["Horse Name"])

# 説明変数と目的変数に分ける
X = merged_table.drop(columns=["Time"])
y = merged_table["Time"]

# 学習用とテスト用に分割 (random_stateは学習時と同じ値を使用)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# データの形式をモデルに合わせる
X_test_jockey = X_test["Jockey"].values
X_test_trainer = X_test["Trainer"].values
X_test_horsename = X_test["Horse Name"].values # Horse Nameを追加
X_test_numeric = X_test.drop(columns=["Jockey", "Trainer", "Horse Name"]).values # Horse Nameをdropに追加
X_test_numeric = X_test_numeric.astype("float32")


# 保存したモデルのパス
model_filepath = "./model/nn_model_with_embedding.keras"

# モデルの読み込み
loaded_model = tf.keras.models.load_model(model_filepath)

# モデルの評価
loss = loaded_model.evaluate([X_test_jockey, X_test_trainer, X_test_horsename, X_test_numeric], y_test, verbose=0)

print(f"Loss: {loss}")


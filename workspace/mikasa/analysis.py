from tabnanny import check
import tensorflow as tf
import tensorflow_probability as tfp
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
import pandas as pd

#  データの読み込み
merged_table = pd.read_csv('./data/merged_table_finished3.csv')

# merged_table['Date']カラムは削除
merged_table = merged_table.drop(['Date'], axis=1)

# Codeカラムは削除
merged_table = merged_table.drop(['Code'], axis=1)


# 1. カテゴリ変数のエンコード
le_jockey = LabelEncoder()
le_trainer = LabelEncoder()
le_horsename = LabelEncoder()
merged_table["Jockey"] = le_jockey.fit_transform(merged_table["Jockey"])
merged_table["Trainer"] = le_trainer.fit_transform(merged_table["Trainer"])
merged_table["Horse Name"] = le_horsename.fit_transform(merged_table["Horse Name"])

# 2. 説明変数と目的変数に分ける
X = merged_table.drop(columns=["Time"])
y = merged_table["Time"]

# 3. 学習用とテスト用に分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

def create_nn_model_with_embedding(numeric_input_shape):
    # JockeyのEmbedding
    jockey_input = tf.keras.layers.Input(shape=(1,), name="Jockey_Input")
    jockey_embed = tf.keras.layers.Embedding(input_dim=len(le_jockey.classes_), output_dim=4)(jockey_input)
    jockey_embed = tf.keras.layers.Flatten()(jockey_embed)

    # TrainerのEmbedding
    trainer_input = tf.keras.layers.Input(shape=(1,), name="Trainer_Input")
    trainer_embed = tf.keras.layers.Embedding(input_dim=len(le_trainer.classes_), output_dim=4)(trainer_input)
    trainer_embed = tf.keras.layers.Flatten()(trainer_embed)

    # Horse NameのEmbedding
    horsename_input = tf.keras.layers.Input(shape=(1,), name="HorseName_Input")
    horsename_embed = tf.keras.layers.Embedding(input_dim=len(le_horsename.classes_), output_dim=4)(horsename_input)
    horsename_embed = tf.keras.layers.Flatten()(horsename_embed)

    # 数値データの入力
    numeric_input = tf.keras.layers.Input(shape=(numeric_input_shape,), name="Numeric_Input")

    # 入力の結合
    x = tf.keras.layers.Concatenate()([jockey_embed, trainer_embed, horsename_embed, numeric_input])

    # 通常の Dense 層を使用
    x = tf.keras.layers.Dense(64, activation="relu")(x) # 変更点
    x = tf.keras.layers.Dense(32, activation="relu")(x) # 変更点
    output = tf.keras.layers.Dense(1)(x) # 変更点

    model = tf.keras.Model(inputs=[jockey_input, trainer_input, horsename_input, numeric_input], outputs=output)
    return model
 
# モデルのインスタンス作成
numeric_input_shape = X_train.drop(columns=["Jockey", "Trainer", "Horse Name"]).shape[1]
nn_model = create_nn_model_with_embedding(numeric_input_shape)

# モデルのコンパイル
nn_model.compile(optimizer="adam", loss="mean_squared_error")

# 6. データの形式をモデルに合わせる
X_train_jockey = X_train["Jockey"].values
X_train_trainer = X_train["Trainer"].values
X_train_horsename = X_train["Horse Name"].values # Horse Nameを追加
X_train_numeric = X_train.drop(columns=["Jockey", "Trainer", "Horse Name"]).values # Horse Nameをdropに追加
X_train_numeric = X_train_numeric.astype("float32")

X_test_jockey = X_test["Jockey"].values
X_test_trainer = X_test["Trainer"].values
X_test_horsename = X_test["Horse Name"].values # Horse Nameを追加
X_test_numeric = X_test.drop(columns=["Jockey", "Trainer", "Horse Name"]).values # Horse Nameをdropに追加
X_test_numeric = X_test_numeric.astype("float32")

# 7. モデルの学習
model_filepath = "./model/nn_model_with_embedding.keras"

# チェックポイントコールバック。`val_loss` が最小となるモデルを保存
checkpoint_callback = tf.keras.callbacks.ModelCheckpoint(
    filepath=model_filepath,
    monitor="val_loss",  # 検証データの損失を監視
    save_best_only=True,  # 最良のモデルのみを保存
    save_weights_only=False, # モデル全体を保存
    verbose=1,  # 保存時にメッセージを表示
    save_freq=100
)

# 早期終了コールバック。`val_loss` が改善しなくなったら学習を停止
early_stopping_callback = tf.keras.callbacks.EarlyStopping(
    monitor="val_loss",  # 検証データの損失を監視
    patience=5,  # 改善が見られないエポック数を指定 (例: 5エポック)
    verbose=1
)

# モデルの学習
history = nn_model.fit( # bnn_model を model に変更
    [X_train_jockey, X_train_trainer, X_train_horsename, X_train_numeric],
    y_train,
    epochs=50, # エポック数は必要に応じて調整
    batch_size=16, # バッチサイズは必要に応じて調整
    validation_data=([X_test_jockey, X_test_trainer, X_test_horsename, X_test_numeric], y_test),
    callbacks=[checkpoint_callback, early_stopping_callback]  # コールバックを指定
)


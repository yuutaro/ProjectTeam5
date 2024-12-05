import pandas as pd
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.model_selection import train_test_split
import numpy as np
import time
import matplotlib.pyplot as plt

# CSVデータの読み込み
data = pd.read_csv("./format_data.csv")

# DataFrameの作成
df1 = pd.DataFrame(data)
df1 = df1[["Rank","Kinryou","Time","Nobori","Ninki","Race Number","Distance","Weight","Weight Change","Ground_ダ","Ground_芝","Ground_障","Condition_不","Condition_稍","Condition_良","Condition_重","Weather_小雨","Weather_小雪","Weather_晴","Weather_曇","Weather_雨","Weather_雪","Sex_セ","Sex_牝","Sex_牡","Age_Under4","Age_Above4"]]

# 特徴量とターゲット変数の定義
X = df1.drop('Time', axis=1)
y = df1['Time']

# 訓練データとテストデータの分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# X_trainとX_testのデータ型をfloat64に変換
X_train = X_train.apply(pd.to_numeric, errors='coerce').fillna(0).astype(np.float64)
X_test = X_test.apply(pd.to_numeric, errors='coerce').fillna(0).astype(np.float64)

# y_trainとy_testのデータ型をfloat64に変換
y_train = y_train.apply(pd.to_numeric, errors='coerce').fillna(0).astype(np.float64)
y_test = y_test.apply(pd.to_numeric, errors='coerce').fillna(0).astype(np.float64)

# モデルの定義
model = Sequential()
model.add(Dense(64, activation='relu', input_shape=(X_train.shape[1],)))
model.add(Dense(32, activation='relu'))
model.add(Dense(1))
model.compile(optimizer='adam', loss='mse')

# 訓練時間の測定
start_time = time.time()

# モデルの訓練
history = model.fit(X_train, y_train, epochs=20, batch_size=32, validation_data=(X_test, y_test))

# 訓練時間の計算
end_time = time.time()
training_time = end_time - start_time

# lossの変化のグラフ
plt.plot(history.history['loss'], label='Training Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')
plt.title('Loss Over Epochs')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()
plt.show()
# モデルの保存
model.save('trained_model.keras')
print(f"Training Time: {training_time} seconds")

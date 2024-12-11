import pandas as pd
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.model_selection import train_test_split
import numpy as np
import time
import matplotlib.pyplot as plt

# CSVデータの読み込み
data = pd.read_csv("../../team2/data/format_data.csv") # team2のデータに統一

# DataFrameの作成
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

# 訓練データとテストデータの分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

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

# モデルの保存
model.save('trained_model.keras')
print(f"Training Time: {training_time} seconds")
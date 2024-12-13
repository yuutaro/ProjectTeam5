import keras
import os
os.environ["KERAS_BACKEND"] = "tensorflow"

import tensorflow as tf
import pandas as pd
import keras 
from keras import layers

from sklearn.model_selection import train_test_split 

# データの読み込み
path = "format_data.csv"
data = pd.read_csv(path)

# # 特徴量とターゲット
features = [
    "Rank","Kinryou","Nobori","Ninki",
    "Race Number","Distance","Weight","Weight Change",
    "Sex","Age","Ground_ダ","Ground_芝","Ground_障","Condition_不",
    "Condition_稍","Condition_良","Condition_重","Weather_小雨","Weather_小雪",
    "Weather_晴","Weather_曇","Weather_雨","Weather_雪"
]
target = "Time_x"
X = data[features]
y = data[target]

# # データの標準化
# scaler = StandardScaler()
# X = scaler.fit_transform(X)

# データの分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
# データの形状に合わせた入力
input_dim = X_train.shape[1]  # 特徴数に基づく

model = keras.Sequential([
    layers.Dense(64, activation='relu', input_shape=(X_train.shape[1],)),
    layers.Dense(32, activation='relu'),
    layers.Dense(1)  # 出力は1次元（レースタイム）
])

# モデルのコンパイル
model.compile(optimizer=keras.optimizers.Adam(learning_rate=0.01), loss='mse', metrics=['mae'])

# モデルの訓練
model.fit(X_train, y_train, epochs=100, verbose=1)

history = model.fit(X_train, y_train, epochs=50, batch_size=32, validation_split=0.2, verbose=1)

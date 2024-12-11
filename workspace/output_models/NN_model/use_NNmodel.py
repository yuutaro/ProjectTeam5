import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error
import tensorflow as tf

# CSVデータの読み込み
data = pd.read_csv("../../team2/data/format_data.csv")

# DataFrameの作成
df = pd.DataFrame(data)

# # 結果を表示df1 = df[["Rank","Kinryou","Time","Nobori","Ninki","Race Number","Distance","Weight","Weight Change","Ground_ダ","Ground_芝","Ground_障","Condition_不","Condition_稍","Condition_良","Condition_重","Weather_小雨","Weather_小雪","Weather_晴","Weather_曇","Weather_雨","Weather_雪","Sex_セ","Sex_牝","Sex_牡","Age_Under4","Age_Above4"]]
# モデルの読み込み
model = tf.keras.models.load_model('trained_model.keras')

# 特徴量データを作成
new_data = pd.DataFrame([{
    "Kinryou": 58.0,
    "Ninki": 7.0,  
    "Race Number": 5,
    "Distance": 1600,
    "Weight": 514,
    "Weight Change": 2,
    "Ground_ダ": 0,
    "Ground_芝": 1,
    "Ground_障": 0,
    "Condition_不": 0,
    "Condition_稍": 0,
    "Condition_良": 1,
    "Condition_重": 0,
    "Weather_小雨": 0,
    "Weather_小雪": 0,
    "Weather_晴": 0,
    "Weather_曇": 1,
    "Weather_雨": 0,
    "Weather_雪": 0,
    "Sex": 0, 
    "Age": 6
}])

# 予測データの前処理
new_data = new_data.apply(pd.to_numeric, errors='coerce').fillna(0).astype(np.float64)
predictions = model.predict(new_data)
print(predictions)

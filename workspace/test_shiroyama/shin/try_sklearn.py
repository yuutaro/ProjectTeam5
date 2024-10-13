import pandas as pd
from sklearn.linear_model import LinearRegression
import re

# CSVファイルからデータを読み込む
df = pd.read_csv('only_num.csv', header=None)
# カラム名を手動で設定
df.columns = ['レース番号', '距離', 'タイム', '一着馬', '天気_小雪', '天気_晴', '天気_曇', '天気_雨', '天気_雪',
              '馬場状態_稍', '馬場状態_良', '馬場状態_重', '馬場_芝', '馬場_障']
# 正規表現パターン
pattern = re.compile(r'^\d{1,2}:\d{1,2}(\.\d+)?$')

# 一致するものだけを残す
df = df[df['タイム'].apply(lambda time: bool(pattern.match(time)))]


# タイムを秒に変換する関数
def convert_time_to_seconds(time_str):
    minutes, seconds = map(float, time_str.split(':'))
    return minutes * 60 + seconds


# タイム列を秒に変換
df['タイム_秒'] = df['タイム'].apply(convert_time_to_seconds)

# 説明変数と目的変数の設定
X = df[['距離', '天気_小雪', '天気_晴', '天気_曇', '天気_雨', '天気_雪',
              '馬場状態_稍', '馬場状態_良', '馬場状態_重', '馬場_芝', '馬場_障']]
y = df['タイム_秒']

# モデルの作成とフィッティング
model = LinearRegression()
model.fit(X, y)

# 回帰係数と切片の表示
coefficients = model.coef_
intercept = model.intercept_

print("回帰係数:", coefficients)
print("切片:", intercept)

# 予測タイムの計算
y_pred = model.predict(X)
df['予測タイム'] = y_pred

# 実際のタイムと予測タイムの比較を表示
print(df[['タイム_秒', '予測タイム']])

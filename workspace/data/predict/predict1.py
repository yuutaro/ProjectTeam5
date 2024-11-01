import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import statsmodels.api as sm

# CSVファイルの読み込み
file_path = 'filtered_data.csv'
df = pd.read_csv(file_path, low_memory=False)

# 説明変数と目的変数の設定
explanatory_variables = ['Weather', 'Condition', 'Sex', 'Age', 'Sta', 'Dis']
target_variable = 'Time_x'

# 説明変数と目的変数の抽出
X = df[explanatory_variables]
y = df[target_variable]

# 繰り返し回数
n_iterations = 10
r2_scores = []
mse_scores = []
mae_scores = []

for _ in range(n_iterations):
    # データを訓練データとテストデータに分割 (80%を訓練、20%をテストに分割)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)  # random_stateを指定しない

    # モデルの作成と訓練
    model = LinearRegression()
    model.fit(X_train, y_train)

    # テストデータでの予測
    y_pred = model.predict(X_test)

    # 評価指標の計算
    mse = mean_squared_error(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    # スコアを保存
    mse_scores.append(mse)
    mae_scores.append(mae)
    r2_scores.append(r2)

# 各評価指標の平均を計算
average_mse = np.mean(mse_scores)
average_mae = np.mean(mae_scores)
average_r2 = np.mean(r2_scores)

# 結果を表示
print("Average Mean Squared Error (MSE):", average_mse)
print("Average Mean Absolute Error (MAE):", average_mae)
print("Average R-squared (R^2):", average_r2)
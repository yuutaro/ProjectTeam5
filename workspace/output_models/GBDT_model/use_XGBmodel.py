import pandas as pd
from sklearn.impute import SimpleImputer
import xgboost as xgb

#他のセルでsave_modelでモデルをxgb_model.jsonとして保存しているので下の＃１でそれを読み込む。save_modelはxgboostのモジュール？を使ってる


# 1. 保存されたモデルを読み込む
xgb_model = xgb.XGBRegressor()
xgb_model.load_model("xgb_model.json")
print("モデルを読み込みました: xgb_model.json")

# # 2. 予測したいレースのデータを受け取る（例として手動で入力）
# new_race_data = pd.DataFrame([{
#     "Kinryou": 58.0,
#     "Distance": 1600,
#     "Weight": 514,
#     "Weight Change": 2,
#     "Age": 6,
#     "Condition_不": 0,
#     "Condition_稍": 0,
#     "Condition_良": 1,
#     "Condition_重": 0,
#     "Weather_小雨": 0,
#     "Weather_小雪": 0,
#     "Weather_晴": 0,
#     "Weather_曇": 1,
#     "Weather_雨": 0,
#     "Weather_雪": 0
# }])

# 特徴量データを作成
new_race_data = pd.DataFrame([{
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

# 3. 欠損値補完
# imputer = SimpleImputer(strategy="most_frequent")
# new_race_data = pd.DataFrame(imputer.fit_transform(new_race_data), columns=new_race_data.columns)

# 4. 予測
predicted_time = xgb_model.predict(new_race_data)
print(f"予測タイム: {predicted_time[0]:.2f}")

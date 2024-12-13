import pandas as pd
from sklearn.impute import SimpleImputer
import xgboost as xgb

# 1. データの読み込み
data = pd.read_csv("../data/format_data.csv")

# 2. 必要な列の抽出（Jockey_xとTrackを除外）
features = [
    "Kinryou", "Distance", "Weight", "Weight Change", 
    "Age", "Condition_不", "Condition_稍", 
    "Condition_良", "Condition_重", "Weather_小雨", "Weather_小雪", 
    "Weather_晴", "Weather_曇", "Weather_雨", "Weather_雪"
]
target = "Time_x"


# 4. 特徴量とターゲットの設定
X = data[features]
y = data[target]

# 5. 欠損値補完
imputer = SimpleImputer(strategy="most_frequent")
X = pd.DataFrame(imputer.fit_transform(X), columns=features)

# 6. XGBoostモデルの構築
xgb_model = xgb.XGBRegressor(
    n_estimators=50,       # ツリーの本数
    learning_rate=0.1,     # 学習率
    max_depth=5,           # ツリーの深さ
    random_state=42,
)

# 7. モデルのトレーニング
xgb_model.fit(X, y)

# 8. モデルをファイルとして保存
xgb_model.save_model("xgb_model.json")
print("モデルを保存しました: xgb_model.json")

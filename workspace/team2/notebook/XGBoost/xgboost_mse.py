import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.metrics import mean_squared_error
import xgboost as xgb

# 1. データの読み込み
data = pd.read_csv("../data/format_data.csv")  # 入力データをCSVから読み込む

# 2. 必要な列の抽出（Jockey_xとTrackを除外）
features = [
    "Kinryou", "Distance", "Weight", "Weight Change", 
    "Age", "Condition_不", "Condition_稍", 
    "Condition_良", "Condition_重", "Weather_小雨", "Weather_小雪", 
    "Weather_晴", "Weather_曇", "Weather_雨", "Weather_雪"
]  # モデルに使用する特徴量
target = "Time_x"  # 予測対象のターゲット変数

# 3. 特徴量とターゲットの設定
X = data[features]  # 特徴量データ
y = data[target]  # ターゲット変数

# 4. 欠損値補完
imputer = SimpleImputer(strategy="most_frequent")  # 最頻値で欠損値を補完
X = pd.DataFrame(imputer.fit_transform(X), columns=features)  # 補完後のデータ

# 5. XGBoostモデルの構築
xgb_model = xgb.XGBRegressor(
    n_estimators=50,       # ツリーの本数
    learning_rate=0.1,     # 学習率
    max_depth=5,           # ツリーの深さ
    random_state=42,       # 乱数シード
)

# 6. モデルのトレーニング
xgb_model.fit(X, y)  # モデルを学習

# 7. タイムを予測
predicted_times = xgb_model.predict(X)  # 予測タイムを計算

# 8. 実際のタイムと予測タイムを比較して表示
comparison = pd.DataFrame({
    "Actual Time": y,          # 実際のタイム
    "Predicted Time": predicted_times  # 予測タイム
})

mean_squared_error(y, predicted_times)




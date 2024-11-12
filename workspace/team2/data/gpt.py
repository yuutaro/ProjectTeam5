import pandas as pd

# データAとデータBのCSVファイルのパス
data_a_path = 'original_data/race_table/combined.csv'  # データAのCSVファイルパス
data_b_path = 'merged_sorted.csv'  # データBのCSVファイルパス

# CSVファイルからデータを読み込む
data_a = pd.read_csv(data_a_path)
data_b = pd.read_csv(data_b_path)

# Code列でデータを結合 (data_bにdata_aの情報を追加)
merged_data = pd.merge(data_b, data_a, on='Code', how='left')
# 不要なデータを除去
merged_data=merged_data.dropna()
merged_data = merged_data.drop(columns=['first_horses'])
merged_data = merged_data.drop(columns=['second_horses'])
merged_data = merged_data.drop(columns=['third_horses'])
merged_data = merged_data.drop(columns=['Time_y'])
merged_data = merged_data.drop(columns=['Jockey_y'])
merged_data = merged_data.drop(columns=['Trainer_y'])
# 結果の確認
# print(merged_data)
merged_data.to_csv('merged_data_final.csv', index=False)

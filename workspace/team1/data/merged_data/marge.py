import pandas as pd
import glob
import re

# 読み込むCSVファイルのパス（パターン指定）を取得し、xの数値部分を基準にソート
file_paths = sorted(
    glob.glob('../original_data/horse_table/*.csv'),  # *.csvのパターンを指定
    key=lambda x: int(re.search(r'race_data_(\d+)_\d+\.csv', x).group(1)) if re.search(r'race_data_(\d+)_\d+\.csv', x) else float('inf')
)

# ソートされたファイルを順に読み込んで結合
dfs = [pd.read_csv(file) for file in file_paths if re.search(r'race_data_(\d+)_\d+\.csv', file)]

# 結合するデータフレームが存在するか確認
if dfs:
    # 全てのデータフレームを縦方向に結合
    merged_df = pd.concat(dfs, ignore_index=True)
    # 結合結果を新しいCSVファイルに保存
    merged_df.to_csv('merged_sorted.csv', index=False)
else:
    print("結合するデータフレームがありません。ファイルのパスや名前を確認してください。")



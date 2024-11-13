import pandas as pd
import glob
import re

data_a_path = 'original_data/race_table/combined.csv'  # データAのCSVファイルパス
data_b_path = 'original_data/horse_table/*.csv'  # データBのCSVファイルパス
# 読み込むCSVファイルのパス（パターン指定）を取得し、xの数値部分を基準にソート
file_paths = sorted(
    glob.glob(data_b_path),  # *.csvのパターンを指定
    key=lambda x: int(re.search(r'race_data_(\d+)_\d+\.csv', x).group(1)) if re.search(r'race_data_(\d+)_\d+\.csv', x) else float('inf')   # type: ignore
)

# ソートされたファイルを順に読み込んで結合
dfs = [pd.read_csv(file) for file in file_paths if re.search(r'race_data_(\d+)_\d+\.csv', file)]

# 結合するデータフレームが存在するか確認
if dfs:
    # 全てのデータフレームを縦方向に結合
    df_b = pd.concat(dfs, ignore_index=True)
    print("馬のデータを結合しました。")
    df_b = df_b.apply(lambda col: col.str.replace('\n', '').replace('\r', '') if col.dtype == 'object' else col)
    print("改行文字を消しました。")
    df_b = df_b[~df_b['Code'].astype(str).str.match(r'^\d{4}$')]
    df_a = pd.read_csv(data_a_path)
    # Code列でデータを結合 (data_bにdata_aの情報を追加)
    merged_df = pd.merge(df_b, df_a, on='Code', how='left')
    print("mergeしました")
    # 不要なデータを除去
    merged_df=merged_df.dropna()
    merged_df = merged_df.drop(columns=['first_horses'])
    merged_df = merged_df.drop(columns=['second_horses'])
    merged_df = merged_df.drop(columns=['third_horses'])
    merged_df = merged_df.drop(columns=['Time_y'])
    merged_df = merged_df.drop(columns=['Jockey_y'])
    merged_df = merged_df.drop(columns=['Trainer_y'])
    merged_df = merged_df[~merged_df['Code'].astype(str).str.match(r'^\d{4}$')]
    merged_df = merged_df.apply(lambda col: col.str.replace('\n', '').replace('\r', '') if col.dtype == 'object' else col)
    # 結合結果を新しいCSVファイルに保存
    merged_df.to_csv('original_data/merged_data.csv', index=False)
else:
    print("結合するデータフレームがありません。ファイルのパスや名前を確認してください。")
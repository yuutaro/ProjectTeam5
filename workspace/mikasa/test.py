import pandas as pd
import json
import glob

# CSVファイルのパスを指定
csv_files = glob.glob('./data/original_data/horse_table/race_data_*.csv')

# 馬の名前を格納するセット
horse_names = set()

# 各CSVファイルを読み込み、馬の名前を抽出
for file in csv_files:
    df = pd.read_csv(file)
    # 'Horse Name'列から馬の名前を取得し、セットに追加
    horse_names.update(df['Horse Name'].unique())

# 重複を排除した馬の名前のリストを作成
unique_horse_names = list(horse_names)

# JSONファイルに書き出す
with open('unique_horse_names.json', 'w', encoding='utf-8') as json_file:
    json.dump(unique_horse_names, json_file, ensure_ascii=False, indent=4)

print(f"重複のない馬の名前を {len(unique_horse_names)} 件、unique_horse_names.json に書き出しました。")
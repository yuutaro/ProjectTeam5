import pandas as pd

# CSVファイルの読み込み
df = pd.read_csv('./data/race_table.csv')  # 適切なファイルパスを指定してください

# Codeカラムが数値型の場合、文字列型に変換してから処理
df['Code'] = df['Code'].astype(str).str.replace(r'\.0$', '', regex=True)


# 変更を新しいCSVファイルとして保存
df.to_csv('./data/race_table2.csv', index=False)  # 新しいファイル名を指定
import pandas as pd
import re
from tqdm import tqdm

file_path = 'merged_data_final.csv'
# CSVファイルの読み込み
df = pd.read_csv(file_path)
# 12桁のコードのみを抽出
df = df[df['Code'].astype(str).str.match(r'^\d{12}$')]

# 正規表現の事前コンパイル（前後にある任意の空白を無視）
time_pattern1 = re.compile(r'\s*(\d+):(\d+\.\d+)\s*')
time_pattern2 = re.compile(r'\s*(\d+):(\d+):(\d+)\s*')
sex_age_pattern = re.compile(r'\s*([牡牝セ])(\d+)\s*')
distance_pattern = re.compile(r'\s*([ダ芝障])(\d+)\s*')
condition_pattern = re.compile(r'\s*([良重稍不])\s*')
weather_pattern = re.compile(r'\s*(晴|曇|小雨|雨|雪|小雪)\s*')
kinryou_pattern = re.compile(r'\s*(\d+)\(([\+\-]?\d+)\)\s*')


# 時間を秒に変換する関数 (ベクトル化)
def time_to_seconds(time_series):
    result = []
    for time_str in time_series:
        if isinstance(time_str, str):
            match1 = time_pattern1.match(time_str)
            if match1:
                minutes, seconds = int(match1.group(1)), float(match1.group(2))
                result.append(minutes * 60 + seconds)
                continue
            match2 = time_pattern2.match(time_str)
            if match2:
                minutes, seconds = int(match2.group(1)), float(match2.group(2))
                result.append(minutes * 60 + seconds)
                continue
        result.append(None)
    return result


# 性別と年齢を抽出する関数（ベクトル化）
def extract_sex_age_column(sex_age_series):
    sexes, ages = [], []
    for text in sex_age_series:
        match = sex_age_pattern.match(text) if isinstance(text, str) else None
        if match:
            sexes.append({'牡': '0', '牝': '1', 'セ': '2'}.get(match.group(1), "unknown"))
            ages.append(int(match.group(2)))
        else:
            sexes.append(None)
            ages.append(None)
    return pd.DataFrame({'Sex': sexes, 'Age': ages})


# 距離を抽出する関数（ベクトル化）
def extract_distance_column(distance_series):
    statuses, distances = [], []
    for text in distance_series:
        match = distance_pattern.match(text) if isinstance(text, str) else None
        if match:
            statuses.append({'ダ': '0', '芝': '1', '障': '2'}.get(match.group(1), "unknown"))
            distances.append(int(match.group(2)))
        else:
            statuses.append(None)
            distances.append(None)
    return pd.DataFrame({'Sta': statuses, 'Dis': distances})


# 条件を抽出する関数（ベクトル化）
def extract_condition_column(condition_series):
    conditions = []
    condition_map = {'良': 0, '重': 1, '稍': 2, '不': 3}  # マッピング
    for text in condition_series:
        match = condition_pattern.match(text) if isinstance(text, str) else None
        if match:
            conditions.append(condition_map.get(match.group(1), None))
        else:
            conditions.append(None)
    return pd.Series(conditions)


# 天気を抽出する関数（ベクトル化）
def extract_weather_column(weather_series):
    weather_map = {'晴': 0, '曇': 1, '小雨': 2, '雨': 3, '雪': 4, '小雪': 5}  # マッピング
    weathers = []
    for text in weather_series:
        match = weather_pattern.match(text) if isinstance(text, str) else None
        if match:
            weathers.append(weather_map.get(match.group(1), None))
        else:
            weathers.append(None)
    return pd.Series(weathers)


# 体重の変化を抽出する関数
def extract_weight_change(weight_series):
    weights, changes = [], []
    for text in weight_series:
        match = re.match(r'(\d+)\(([\+\-]?\d+)\)', text) if isinstance(text, str) else None
        if match:
            weights.append(int(match.group(1)))  # 体重
            changes.append(int(match.group(2)))  # 変化量
        else:
            weights.append(None)
            changes.append(None)
    return pd.DataFrame({'Weight': weights, 'Change': changes})



# tqdmの進捗バーを使用して変換
tqdm.pandas()
df['Time_x'] = time_to_seconds(df['Time_x'].values)

# SexとAgeの列に分割して格納
sex_age_df = extract_sex_age_column(df['Sex/Age'].values)
df[['Sex', 'Age']] = sex_age_df

# StaとDisの列に分割して格納
distance_df = extract_distance_column(df['Distance'].values)
df[['Sta', 'Dis']] = distance_df

# Conditionの列に分割して格納
df['Condition'] = extract_condition_column(df['Condition'].values)

# Weatherの列に分割して格納
df['Weather'] = extract_weather_column(df['Weather'].values)
# 新しいカラム 'Horse Weight' を追加して処理
weight_change_df = extract_weight_change(df['Horse Weight'].values)
df[['Weight', 'Change']] = weight_change_df

# NaN 値が含まれている行をフィルタリング
df = df.dropna(subset=['Sex', 'Age', 'Sta', 'Dis', 'Condition', 'Weather'])

# 不要な列を削除
df = df.drop('Sex/Age', axis=1)
df = df.drop('Distance', axis=1)

# フィルタリングしたデータをCSVに保存
df.to_csv('filtered_data.csv', index=False)
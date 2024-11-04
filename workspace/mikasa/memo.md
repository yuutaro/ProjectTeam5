| Column Name         | Data Type | Description                                    | null    |
| ------------------- | --------- | ---------------------------------------------- | ------- |
| Code                | int64     | レースの識別番号                               | 0       |
| Rank                | int64     | レースにおける順位                             | 0       |
| Frame Rank          | int64     | フレーム内での順位                             | 0       |
| Horse Number        | int64     | 馬の番号                                       | 0       |
| Horse Name          | object    | 馬の名前                                       | 0       |
| Kinryou             | float64   | 馬の斤量（体重）                               | 0       |
| Jockey              | object    | ジョッキーの名前                               | 0       |
| Time                | float64   | レースの所要時間（秒数）                       | 0       |
| Chakusa             | object    | 着順（フォーマットによる）                     | 904084  |
| Nobori              | float64   | 上昇度（成績の向上を示す指標）                 | 2021595 |
| Tansyou             | float64   | 単勝オッズ                                     | 1659530 |
| Ninki               | float64   | 人気（馬の人気度）                             | 46      |
| Horse Weight        | float64   | 馬の体重（斤量）                               | 3547    |
| Trainer             | object    | トレーナーの名前                               | 0       |
| Banushi             | object    | 馬主の名前                                     | 96709   |
| Shoukin             | object    | 賞金                                           | 3167645 |
| Date                | object    | レース日（通常は文字列形式）                   | 0       |
| Track               | object    | トラックの種類                                 | 0       |
| Weather             | object    | 天候                                           | 0       |
| Race Number         | int64     | レースの番号                                   | 0       |
| Distance            | int64     | レースの距離（メートル単位）                   | 0       |
| Condition           | object    | トラックコンディション                         | 387819  |
| Disqualification    | int64     | 失格の有無（失格の場合は 1、そうでなければ 0） | 0       |
| Sex                 | int64     | 馬の性別（数値で表現）                         | 0       |
| Age                 | int64     | 馬の年齢（数値で表現）                         | 0       |
| Track Type          | object    | トラックのタイプ                               | 0       |
| intermediate_rank_1 | float64   | 中間順位 1                                     | 1072605 |
| intermediate_rank_2 | float64   | 中間順位 2                                     | 1116477 |
| intermediate_rank_3 | float64   | 中間順位 3                                     | 2367017 |
| intermediate_rank_4 | float64   | 中間順位 4                                     | 3182497 |
| Horse Weight Change | int64     | 馬の体重の変化（斤量の増減）                   | 0       |
| Trainers Stable     | object    | トレーナーの厩舎名                             | 0       |

# Selenium 4
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
import pandas as pd
from time import sleep

DRIVER_PATH = "C:./chromedriver-win64/chromedriver.exe"
RACE_LIST_BASE_URL = "https://db.netkeiba.com/?pid=race_list&word=&start_year=1986&start_mon=none&end_year=2024&end_mon=9&kyori_min=&kyori_max=&sort=date&list=20&page="
MAX_PAGE_NUM = 30750
START_PAGE_NUM = 1
END_PAGE_NUM = 10000

def init_driver():
  options = webdriver.ChromeOptions()
  service = ChromeService(DRIVER_PATH)
  driver = webdriver.Chrome(service=service, options=options)
  return driver

# ドライバーを初期化
driver = init_driver()

# テーブルのプライマリキーの初期値
current_id = 1
current_horse_id = 1

# レースと馬の辞書を保存するリスト
race_data = []
horse_data = []

# ページ数分だけ繰り返す
for page_num in range(START_PAGE_NUM, END_PAGE_NUM + 1):
  # レース一覧ページを開く
  driver.get(RACE_LIST_BASE_URL + str(page_num))

  # レース一覧ページのテーブルを取得
  tbody = driver.find_element(By.TAG_NAME, "tbody")

  # レース一覧ページのテーブルの行を取得
  trs = tbody.find_elements(By.TAG_NAME, "tr")

  i = len(trs) - 1

  for i in range(1, len(trs)):
    tbody = driver.find_element(By.TAG_NAME, "tbody")
    trs = tbody.find_elements(By.TAG_NAME, "tr")
    tr = trs[i]
    tds = tr.find_elements(By.TAG_NAME, "td")
    
    # レース一覧ページのテーブルの行の各セルのテキストを取得
    id = current_id
    date = tds[0].text
    place = tds[1].text
    weather = tds[2].text
    round = tds[3].text
    race_name = tds[4].text
    distance = tds[6].text
    horse_num = tds[7].text
    track_condition = tds[8].text
    time = tds[9].text
    pase = tds[10].text
    first = tds[11].text
    second = tds[14].text
    third = tds[15].text

    race_data.append({
      "id": id,
      "date": date,
      "place": place,
      "weather": weather,
      "round": round,
      "race_name": race_name,
      "distance": distance,
      "horse_num": horse_num,
      "track_condition": track_condition,
      "time": time,
      "pase": pase,
      "first": first,
      "second": second,
      "third": third
    })

    # このレースの詳細ページに移動し、Horseインスタンスを作成
    tds[4].find_element(By.TAG_NAME, "a").click()

    # レース詳細ページのテーブルを取得
    race_tbody = driver.find_element(By.TAG_NAME, "tbody")

    # レース詳細ページのテーブルの行を取得
    race_trs = race_tbody.find_elements(By.TAG_NAME, "tr")

    for race_tr in race_trs[1:]:
      # レース詳細ページのテーブルの行の各セルを取得
      race_tds = race_tr.find_elements(By.TAG_NAME, "td")

      # セルのテキストを取得するためのヘルパー関数
      def get_td_text(tds, index):
          try:
              return tds[index].text
          except IndexError:
              return ""  # 要素が存在しない場合は空文字を返す

      # 各変数に値を代入
      id = current_horse_id
      race_id = current_id
      rank = get_td_text(race_tds, 0)
      post_position = get_td_text(race_tds, 1)
      horse_number = get_td_text(race_tds, 2)
      horse_name = get_td_text(race_tds, 3)
      sex_age = get_td_text(race_tds, 4)
      weight = get_td_text(race_tds, 5)
      jockey = get_td_text(race_tds, 6)
      time = get_td_text(race_tds, 7)
      winning_margin = get_td_text(race_tds, 8)
      sector_rank = get_td_text(race_tds, 10)
      last_3f = get_td_text(race_tds, 11)
      single_odds = get_td_text(race_tds, 12)
      body_weight = get_td_text(race_tds, 14)
      trainer = get_td_text(race_tds, 18)
      owner = get_td_text(race_tds, 19)
      earning = get_td_text(race_tds, 20)

      horse_data.append({
        "id": id,
        "race_id": race_id,
        "rank": rank,
        "post_position": post_position,
        "horse_number": horse_number,
        "horse_name": horse_name,
        "sex_age": sex_age,
        "weight": weight,
        "jockey": jockey,
        "time": time,
        "winning_margin": winning_margin,
        "sector_rank": sector_rank,
        "last_3f": last_3f,
        "single_odds": single_odds,
        "body_weight": body_weight,
        "trainer": trainer,
        "owner": owner,
        "earning": earning
      })

      current_horse_id += 1

      # 一旦確認
      # print("id: ", id)
      # print("race_id: ", race_id)
      # print("rank: ", rank)
      # print("post_position: ", post_position)
      # print("horse_number: ", horse_number)
      # print("horse_name: ", horse_name)
      # print("sex_age: ", sex_age)
      # print("weight: ", weight)
      # print("jockey: ", jockey)
      # print("time: ", time)
      # print("winning_margin: ", winning_margin)
      # print("sector_rank: ", sector_rank)
      # print("last_3f: ", last_3f)
      # print("single_odds: ", single_odds)
      # print("body_weight: ", body_weight)
      # print("trainer: ", trainer)
      # print("owner: ", owner)
      # print("earning: ", earning)
      # print() 

    # レース詳細ページからレース一覧ページに戻る
    driver.get(RACE_LIST_BASE_URL + str(page_num))

    # tbody,trsを再取得
    tbody = driver.find_element(By.TAG_NAME, "tbody")
    trs = tbody.find_elements(By.TAG_NAME, "tr")

    # 一旦確認
    # print("id: ", current_id)
    # print("date: ", date)
    # print("place: ", place)
    # print("weather: ", weather)
    # print("round: ", round)
    # print("race_name: ", race_name)
    # print("distance: ", distance)
    # print("horse_num: ", horse_num)
    # print("track_condition: ", track_condition)
    # print("time: ", time)
    # print("pase: ", pase)
    # print("first: ", first)
    # print("second: ", second)
    # print("third: ", third)
    # print()

    print(f"Page number: {page_num}, Race number: {(page_num - 1) * 20 + i}, Race number on page: {i}")

    current_id += 1

races_df = pd.DataFrame(race_data)
horses_df = pd.DataFrame(horse_data)

races_df.to_csv("races.csv", index=False, encoding='utf-8-sig')
horses_df.to_csv("horses.csv", index=False, encoding='utf-8-sig')

driver.quit()
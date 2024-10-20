
import requests
from bs4 import BeautifulSoup
import pandas as pd
from lxml import html
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor, as_completed
import time  # リトライ用に必要

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}

race_data = []
start_page = 1301  # 開始ページ
end_page = 2001  # 終了ページ+1（1000ページ分）
max_workers = 10  # スレッドの数
pages_per_save = 10  # データを保存する頻度（10ページごと）


def extract_race_data(columns):
    """列からレースデータを抽出して辞書形式で返す"""
    return {
        "Rank": columns[0].get_text(strip=True) if len(columns) > 0 else None,
        "Frame Rank": columns[1].get_text(strip=True) if len(columns) > 1 else None,
        "Horse Number": columns[2].get_text(strip=True) if len(columns) > 2 else None,
        "Horse Name": columns[3].get_text(strip=True) if len(columns) > 3 else None,
        "Sex/Age": columns[4].get_text(strip=True) if len(columns) > 4 else None,
        "Kinryou": columns[5].get_text(strip=True) if len(columns) > 5 else None,
        "Jockey": columns[6].get_text(strip=True) if len(columns) > 6 else None,
        "Time": columns[7].get_text(strip=True) if len(columns) > 7 else None,
        "Chakusa": columns[8].get_text(strip=True) if len(columns) > 8 else None,
        "Tsuuka": columns[10].get_text(strip=True) if len(columns) > 9 else None,
        "Nobori": columns[11].get_text(strip=True) if len(columns) > 10 else None,
        "Tansyou": columns[12].get_text(strip=True) if len(columns) > 11 else None,
        "Ninki": columns[13].get_text(strip=True) if len(columns) > 12 else None,
        "Horse Weight": columns[14].get_text(strip=True) if len(columns) > 13 else None,
        "Trainer": columns[18].get_text(strip=True) if len(columns) > 14 else None,
        "Banushi": columns[19].get_text(strip=True) if len(columns) > 15 else None,
        "Shoukin": columns[20].get_text(strip=True) if len(columns) > 16 else None
    }


def get_race_urls(page_url):
    """ページからレースURLを取得"""
    for _ in range(3):  # リトライは3回まで
        try:
            response = requests.get(page_url, headers=headers)
            response.raise_for_status()
            tree = html.fromstring(response.content)
            return tree.xpath('//div[@id="contents_liquid"]//td[@class="txt_l"]/a[contains(@href, "/race")]/@href')
        except requests.exceptions.RequestException as e:
            print(f"Error fetching race list from {page_url}: {e}. Retrying...")
            time.sleep(5)  # 5秒待ってリトライ
    return []


def fetch_race_data(url):
    """レースURLからデータを取得し、フィルタリングしたデータを返す"""
    full_url = f"https://db.netkeiba.com{url}"
    try:
        response = requests.get(full_url, headers=headers)
        response.raise_for_status()
        response.encoding = response.apparent_encoding
        soup = BeautifulSoup(response.text, 'html.parser')
        rows = soup.find_all('tr')
        race_data = []

        for row in rows:
            columns = row.find_all('td')
            data = extract_race_data(columns)

            # フィルタリング: タイムデータが存在するレコードのみ追加
            if data["Time"] is not None and data["Rank"] is not None:
                race_data.append(data)

        return race_data

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from {full_url}: {e}")
        return []


def save_data(data, start, end):
    """取得したデータをCSVに保存"""
    df = pd.DataFrame(data)
    df = df[df['Time'] != ""]  # Time列が空の行を削除
    filename = f"race_data_{start}_{end - 1}.csv"
    df.to_csv(filename, index=False, encoding='utf-8-sig')
    print(f"Data saved to {filename}")


# 全レースURLを収集して処理
base_url_template = 'https://db.netkeiba.com/?pid=race_list&word=&start_year=1985&start_mon=none&end_year=2024&end_mon=9&kyori_min=&kyori_max=&sort=date&list=100&page='

for batch_start_page in range(start_page, end_page, pages_per_save):
    batch_end_page = min(batch_start_page + pages_per_save, end_page)

    race_urls = []

    # ページごとにURL収集
    for number in range(batch_start_page, batch_end_page):
        base_url = f"{base_url_template}{number}"
        race_urls.extend(get_race_urls(base_url))

    # 並列処理でレースデータを取得
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = [executor.submit(fetch_race_data, url) for url in race_urls]

        batch_race_data = []
        for future in tqdm(as_completed(futures), total=len(futures),
                           desc=f"Fetching Race Data (Pages {batch_start_page}-{batch_end_page - 1})"):
            result = future.result()
            if result:
                batch_race_data.extend(result)

    # データをCSVに保存
    save_data(batch_race_data, batch_start_page, batch_end_page)


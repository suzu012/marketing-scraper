import requests
from bs4 import BeautifulSoup
from datetime import datetime
import csv
import pytz

# 日本時間で現在時刻を取得
jst = pytz.timezone('Asia/Tokyo')
now = datetime.now(jst)
timestamp = now.strftime("%Y-%m-%d_%H-%M-%S")

# 取得したいニュースのRSS URL（今回はマーケティング情報）
url = "https://markezine.jp/rss/new/"

# RSSデータを取得
response = requests.get(url)
soup = BeautifulSoup(response.content, "xml")
items = soup.find_all("item")

# ファイル名を作成（例：marketing_2025-04-07_08-30-12.csv）
filename = f"marketing_{timestamp}.csv"

# CSVファイルに保存
with open(filename, "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["日付", "タイトル", "URL"])  # ヘッダー行
    for item in items:
        title = item.title.text
        link = item.link.text
        writer.writerow([now.strftime("%Y-%m-%d"), title, link])

print(f"✅ {filename} に保存しました！（{now.strftime('%H:%M:%S')} に実行）")


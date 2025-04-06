import requests
from bs4 import BeautifulSoup
from datetime import datetime
import csv
import pytz

# 日本時間を取得
jst = pytz.timezone('Asia/Tokyo')
now = datetime.now(jst)
today = now.strftime("%Y-%m-%d")

# RSSデータを取得
url = "https://news.yahoo.co.jp/rss/topics/top-picks.xml"
response = requests.get(url)
soup = BeautifulSoup(response.content, "xml")
items = soup.find_all("item")

# ファイル名を作成
filename = f"marketing_{today}.csv"

# CSVファイルに保存
with open(filename, "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["日付", "タイトル", "URL"])
    for item in items:
        title = item.title.text
        link = item.link.text
        writer.writerow([today, title, link])

print(f"✅ {filename} に保存しました！")

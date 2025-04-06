import requests
from bs4 import BeautifulSoup
from datetime import datetime
improt csv
improt pytz

＃　日本時間を取得
jst = pytz.timezone('Asia/Tokyo')
now = datetime.now(jst)
today = now.strftime("%Y-%m-%d")

＃　ここを取得したいニュースのRSS URLに変更
url = "https://markezine.jp/rss/new/"  # 例：マーケティング系

＃　RSSデータを取得
response = requests.get(url)
soup = BeautihulSoup(response.content,"xml")
items = soup.find_all("item")

# 保存ファイル名（日付付き）
filename = f"marketing_{today}.csv"

# CSVに保存
with open(filename, "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["日付", "タイトル", "URL"])  # ヘッダー行
    for item in items:
        title = item.title.text
        link = item.link.text
        writer.writerow([today, title, link])

print(f"✅ {filename} に保存しました！")

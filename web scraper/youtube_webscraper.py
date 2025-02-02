import requests
from bs4 import BeautifulSoup
import csv
from requests_html import HTML, HTMLSession
raw_html = requests.get("https://www.youtube.com/user/schafer5/videos").text

soup = BeautifulSoup(raw_html, 'lxml')
video_data = []
channel = soup.title.text
channel = channel.replace("- YouTube", "").strip()
video_data.append(channel)

for detail in soup.find_all('div', class_='yt-lockup-content'):
    video_title = detail.h3.a.text
    video_views = detail.div.ul.li.text
    video_views = video_views.replace(" views", "")
    video_data.append((video_title, video_views))

with open(f"{video_data[0]}_yt_data.csv", "w+", newline="", encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(("Title", "Views"))
    for v in video_data:
        if v == video_data[0]:
            pass
        else:
            csv_writer.writerow(v)

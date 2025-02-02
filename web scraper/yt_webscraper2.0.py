import csv
import time
import re
from selenium import webdriver
from bs4 import BeautifulSoup
from tqdm import tqdm

urls = [
    #'https://www.youtube.com/channel/UCzmkeda2XiYpETOP5MjotrQ/videos',
    'https://www.youtube.com/user/PewDiePie/videos',
    #'https://www.youtube.com/user/tseries/videos'
]

for url in tqdm(urls):
    def find_views(html_to_search):
        pattern = re.compile(r'\d+\s[v]|\d+,\d+\s[v]|\d+,\d+,\d+\s[v]')
        match = re.findall(pattern, str(html_to_search))
        return match


    browser = webdriver.Chrome()
    browser.get(url)

    current_height = 0
    while True:
        browser.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
        last_height = browser.execute_script("return document.documentElement.scrollHeight")
        time.sleep(3)
        if last_height == current_height:
            break
        else:
            current_height = last_height

    html = browser.page_source
    browser.close()

    soup = BeautifulSoup(html, 'lxml')
    video_data = []

    channel = soup.title.text
    channel = channel.replace("- YouTube", "").strip()
    video_data.append(channel)
    video_titles = []
    for result in soup.find_all('a', class_='yt-simple-endpoint style-scope ytd-grid-video-renderer'):
        video_titles.append(result.text)
    video_views = []
    for result in soup.find_all('a', class_='yt-simple-endpoint style-scope ytd-grid-video-renderer'):
        m = find_views(result)
        try:
            view_count = m[0].replace(" v", "")
        except IndexError:
            print(result)
            print(m)
            view_count = 0
        video_views.append(view_count)

    for title, view in zip(video_titles, video_views):
        video_data.append((title, view))

    try:
        with open(f"{video_data[0]}_yt_data.csv", "w+", newline="", encoding='utf-8') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(("Title", "Views"))
            for v in video_data:
                if v == video_data[0]:
                    pass
                else:
                    try:
                        csv_writer.writerow(v)
                    except UnicodeEncodeError:
                        print(v)
                        pass
    except PermissionError as e:
        print(e)
    except FileNotFoundError as e:
        print(e)
    except OSError as e:
        print(e)

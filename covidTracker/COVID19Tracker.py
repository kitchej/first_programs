import csv
import time
import re
import requests
import csv
from datetime import date
from bs4 import BeautifulSoup
import schedule


def get_info():
    html = requests.get("https://en.wikipedia.org/wiki/2019%E2%80%9320_coronavirus_pandemic_by_country_and_territory").text
    soup = BeautifulSoup(html, 'lxml')
    container = soup.find(id="covid19-container")
    table = container.table
    table_names = table.find_all(scope="row")

    country_names = []
    for name in table_names:
        if name.a is None:
            pass
        else:
            country_names.append(name.a.text)

    numbers = table.find_all("td")
    pattern = re.compile(r'\d+,\d+')
    pattern2 = re.compile(r'\d+')
    raw_data = []
    for number in numbers:
        if pattern.fullmatch(number.text.strip("\n")):
            raw_data.append(number.text.strip("\n"))
        elif pattern2.fullmatch(number.text.strip("\n")):
            raw_data.append(number.text.strip("\n"))
        elif number.text.strip("\n") == "–":
            raw_data.append("0")
        else:
            pass

    data = []
    i = 0
    for _ in range(int((len(country_names)/3))):
        data.append((int(raw_data[i].replace(",", "")),
                     int(raw_data[i+1].replace(",", "")),
                     int(raw_data[i+2].replace(",", ""))))
        i += 3

    with open(f"Data/covid19_data_{date.today()}.csv", "w+", encoding="utf-8", newline="") as file:
        csv_writer = csv.writer(file)
        for entry, name in zip(data, country_names):
            csv_writer.writerow([name, entry])
    print(f"Data for {date.today()} collected")

schedule.every().day.at("21:38").do(get_info)
print("DO NOT CLOSE - DATA COLLECTION IN PROGRESS")
print(f"Collecting since {date.today()}")
while True:
    schedule.run_pending()
    

import requests
import re
from datetime import date, datetime
import socket
from bs4 import BeautifulSoup


def get_info():
    out = []
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
    for entry, name in zip(data, country_names):
            out.append([name, entry])
    return out

def live_report(report_time):
    data = get_info()
    for entry in data:
        if "United States" in entry:
            stats = entry[1]
            us_data = [int(stats[0]), int(stats[1]), int(stats[2])]
            
    cases = []
    deaths = []
    recoveries = []

    for entry in data:
        stats = entry[1]
        cases.append(stats[0])
        deaths.append(stats[1])
        recoveries.append(stats[2])
    total_cases = 0
    total_deaths = 0
    total_recoveries = 0
    for c, d, r in zip(cases, deaths, recoveries):
        total_cases += int(c)
        total_deaths += int(d)
        total_recoveries += int(r)

    world_data = [total_cases, total_deaths, total_recoveries]
    
    template = f"\
    {report_time}\n\
    -------------------\n\
    UNITED STATES\n\
    TOTAL CASES: {us_data[0]}\n\
    TOTAL DEATHS: {us_data[1]}\n\
    TOTAL RECOVERIES: {us_data[2]}\n\
    --------------------\n\
    WORLDWIDE\n\
    TOTAL CASES: {world_data[0]}\n\
    TOTAL DEATHS: {world_data[1]}\n\
    TOTAL RECOVERIES: {world_data[2]}\n\
    "
    return template


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    HOST = '10.0.0.186'
    PORT =  4000
    s.bind((HOST, PORT))
    while True:
        s.listen()
        print("Listening...")
        connection, address = s.accept()
        while True:
            try:
                msg = live_report(datetime.now().strftime('%m/%d/%Y %I:%M %p'))
                connection.send(bytes(msg, 'utf-8'))
            except ConnectionResetError:
                print("Client disconnected")
                break
            except ConnectionAbortedError:
                print("Connection Aborted")
                break
            except OSError:
                break


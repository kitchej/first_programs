import requests
import re
from datetime import date
import os
import schedule
from bs4 import BeautifulSoup
import COVID19analiysis as covid


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


def get_news():
    html = requests.get(
        "https://www.google.com/search?q=coronavirus&rlz=1C1CHBF_enUS785US785&sxsrf=ALeKk02WpC29a9DEkDUOor2kL65DqoP8zA:"
        "1585619256304&source=lnms&tbm=nws&sa=X&ved=2ahUKEwi-_5SEzMPoAhVRqZ4KHamMDxUQ_AUoAXoECBQQAw&biw=853&bih=657"
    ).text
    soup = BeautifulSoup(html, 'lxml')
    headlines = soup.find_all("div", class_="BNeawe vvjwJb AP7Wnd")
    out = [headline.text for headline in headlines]
    return out


def end_of_day_report():
    us_data = covid.get_country_data_day("United States", -1)
    us_yesterday = covid.get_country_data_day("United States", -2)
    
    world_data = covid.get_world_day_total(-1)
    world_yesterday = covid.get_world_day_total(-2)
    news = get_news()
    headlines = ""
    for story in news:
        headlines = headlines + f"* {story}\n"
    template = f"\
    \n\
    END OF DAY REPORT {date.today().strftime('%m/%d/%Y')}\n\
    ---------------------\n\
           NEWS\n\
           \n\
{headlines}\n\
    ---------------------\n\
        UNITED STATES\n\
    TOTAL CASES: {us_data[0]}\n\
    TOTAL DEATHS: {us_data[1]}\n\
    TOTAL RECOVERIES: {us_data[2]}\n\
    \n\
    CASES UP BY: {int(us_data[0]) - int(us_yesterday[0])}\n\
    DEATHS UP BY: {int(us_data[1]) - int(us_yesterday[1])}\n\
    RECOVERIES UP: BY {int(us_data[2]) - int(us_yesterday[2])}\n\
    ---------------------\n\
          WORLDWIDE\n\
    TOTAL CASES: {world_data[0]}\n\
    TOTAL DEATHS: {world_data[1]}\n\
    TOTAL RECOVERIES: {world_data[2]}\n\
    \n\
    CASES UP BY: {int(world_data[0]) - int(world_yesterday[0])}\n\
    DEATHS UP BY: {int(world_data[1]) - int(world_yesterday[1])}\n\
    RECOVERIES UP BY: {int(world_data[2]) - int(world_yesterday[2])}\n\
    "
    print(template)


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
    
    news = get_news()
    headlines = ""
    for story in news:
        headlines = headlines + f"* {story}\n"
        
    template = f"\
    {report_time} REPORT {date.today().strftime('%m/%d/%Y')}\n\
    ---------------------\n\
           NEWS\n\
    \n\
{headlines}\n\
    ---------------------\n\
        UNITED STATES\n\
    TOTAL CASES: {us_data[0]}\n\
    TOTAL DEATHS: {us_data[1]}\n\
    TOTAL RECOVERIES: {us_data[2]}\n\
    ---------------------\n\
          WORLDWIDE\n\
    TOTAL CASES: {world_data[0]}\n\
    TOTAL DEATHS: {world_data[1]}\n\
    TOTAL RECOVERIES: {world_data[2]}\n\
    "
    print(template)

live_report("MORNING REPORT")
schedule.every().day.at("12:00").do(live_report, "MID-DAY")
schedule.every().day.at("18:00").do(live_report, "EVENING")   
schedule.every().day.at("23:59").do(end_of_day_report)
while True:
    schedule.run_pending()

import csv
import os


class InputError(Exception):
    def __init__(self, message):
        self.message = message

def get_data():
    csv_files = os.listdir("Data")
    csv_files.sort()
    out = [[] for i in range(len(csv_files))]
    n = 0
    for csv_file in csv_files:
        with open(f"Data/{csv_file}") as file:
            csv_reader = csv.reader(file)
            for line in csv_reader:
                out[n].append(line)
            n += 1
    return out


def get_country_data(country):  # Returns a list of stats for one country over the entire collection period
    country_total = []
    total_data = get_data()
    for day in total_data:
        for entry in day:
            if entry[0] == country:
                stats = entry[1].split(", ")
                country_total.append(
                [int(stats[0].replace("(", "")), int(stats[1]), int(stats[2].replace(")", ""))])
    if country_total:
        pass
    else:
        raise InputError(f"\'{country}\' does not exist in the data set. Country name must be typed how it "
                         f"appears in the wikipedia article. \'world\' must be lowercase")
    return country_total  # [[data, data, data], [data, data, data], .....]


def get_country_data_day(country, day):  # Returns a list of stats for one country in one day
    total_data = get_data()
    for entry in total_data[day]:
        if entry[0] == country:
            stats = entry[1]
            stats = stats.split(", ")
            day_total = [int(stats[0].replace("(", "")), int(stats[1]), int(stats[2].replace(")", ""))]
            return day_total


def get_single_stat_country(country, stat_type):  # Returns numbers for one stat for one country over the
    data = get_country_data(country)  # collection period
    out = []
    for entry in data:
        if stat_type == "cases":
            out.append(entry[0])
        elif stat_type == "deaths":
            out.append(entry[1])
        elif stat_type == "recoveries":
            out.append(entry[2])
        else:
            raise InputError(f"\'{stat_type}\' is not valid. Must be \'cases\', \'deaths\', "
                             f"or \'recoveries'")
    return out


def get_world_day_total(date):  # Returns total cases, deaths, and recoveries worldwide for a single day
    cases = []
    deaths = []
    recoveries = []
    total_data = get_data()
    for entry in total_data[date]:
        stats = entry[1]
        stats = stats.split(", ")
        cases.append(stats[0].replace("(", ""))
        deaths.append(stats[1])
        recoveries.append(stats[2].replace(")", ""))
    total_cases = 0
    total_deaths = 0
    total_recoveries = 0
    for c, d, r in zip(cases, deaths, recoveries):
        total_cases += int(c)
        total_deaths += int(d)
        total_recoveries += int(r)
    return [total_cases, total_deaths, total_recoveries]


def get_world_total():  # Returns a list of total world stats for each day in the collection period
    stats = []
    total_data = get_data()
    for i in range(len(total_data)):
        stats.append(get_world_day_total(i))
    return stats  # [[data, data, data], [data, data, data] .......]


def get_single_stat_world(stat_type):  # Returns numbers for one stat worldwide over the
    data = get_world_total()  # collection period
    out = []
    for entry in data:
        if stat_type == "cases":
            out.append(entry[0])
        elif stat_type == "deaths":
            out.append(entry[1])
        elif stat_type == "recoveries":
            out.append(entry[2])
        else:
            raise InputError(f"\'{stat_type}\' is not valid. Must be \'cases\', \'deaths\', "
                             f"or \'recoveries\'")
    return out


def get_stat_per_day(country, stat):  # Returns number of new cases/deaths/recoveries per day in the collection period
    stat_per_day = []
    if country == "world":
        data = get_single_stat_world(stat)
    else:
        data = get_single_stat_country(country, stat)
    for i in range(len(data)):
        if i == 0:
            stat_per_day.append(0)
        else:
            increase = data[i] - data[i - 1]
            stat_per_day.append(increase)
    return stat_per_day

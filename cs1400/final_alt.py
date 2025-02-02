"""
Project Name: Project 7 - Was Clinton Right?
Author: Joshua Kitchen
Due Date: 12/7/2020
Course: CS1400-005
"""
import csv
from matplotlib import pyplot as plt


"""
John F. Kennedy,D,1-1961 11-1963
Lyndon B. Johnson,D,12-1963 1-1969
Richard M. Nixon,R,2-1969 7-1974
Gerald R. Ford,R,8-1974 1-1977
Jimmy Carter,D,2-1977 1-1981
Ronald Reagan,R,2-1981 1-1989
George Bush,R,2-1989 1-1993
Bill Clinton,D,2-1993 1-2001
George W. Bush,R,2-2001 1-2009
Barack Obama,D,2-2009 10-2012
"""


# Calculates new jobs per month. Returns a dict of years mapped to a with a dict of months and new jobs
def monthly_change(data):
    month_change_dict = {}
    prev = 0
    for item in data:
        month_change = {}
        month_count = 1
        for i in data[item]:
            if prev == 0:
                month_change.update({month_count: 0})
            else:
                month_change.update({month_count: int(i) - int(prev)})
            prev = i
            month_count += 1
        month_change_dict[item] = month_change
    print(month_change_dict)
    return month_change_dict


def yearly_change(data):
    out = {}
    for i in data.keys():
        yearly_jobs = 0
        for m in data[i]:
            yearly_jobs += int(data[i][m])
        out.update({i: yearly_jobs})
    return out


def new_jobs_by_pres(data, presidents_dict, president):
    jobs = 0
    _range = presidents_dict[president][1]
    start = _range[0].split('-')
    end = _range[1].split('-')
    year_start = int(start[1])
    month_start = int(start[0])
    year_end = int(end[1])
    month_end = int(end[0])
    last_year = False

    for _ in range(4):
        if year_start == year_end:
            last_year = True
        for _ in range(11):
            if month_start == 12:
                break
            if last_year:
                if month_start == month_end:
                    break
            jobs += data[str(year_start)][month_start]
            month_start += 1

        year_start += 1
    print(jobs)

    # while year_start <= year_end:
    #     if year_start == year_end:
    #         months = month_end
    #     while month_start <= months:
    #         jobs += data[str(year_start)][month_start]
    #         month_start += 1
    #     year_start += 1
    # print(jobs)
    # return jobs


def new_jobs_by_party(data, presidents_dict, party):
    jobs = 0
    for president in presidents_dict:
        if presidents_dict[president][0] == party:
            if data[president] is None:
                continue
            jobs += data[president]
    return jobs, jobs / 5


def main():
    file_name = 'BLS_private.csv'
    presidents_file = 'presidents.txt'

    # Get data
    data = []
    try:
        with open(file_name, 'r') as file:
            csv_reader = csv.reader(file)
            for item in csv_reader:
                data.append(item)
    except FileNotFoundError:
        print(f'\'{file_name}\' does not exist')
        return
    except PermissionError:
        print("Error opening file")
        return
    except OSError:
        print("Error reading file")
        return

    # Convert to Dictionary
    jobs_data = {}
    for line in data:
        key = line.pop(0)
        jobs_data[key] = line

    # Get president info - Example: 'John F. Kennedy': ('D', ['1-1961', '11-1963'])

    presidents = {}

    try:
        with open(presidents_file, 'r') as file:
            for line in file.readlines():
                info = line.split(',')
                presidents.update({info[0]: (info[1], info[2].split())})
    except FileNotFoundError:
        print(f'\'{presidents_file}\' does not exist')
        return
    except PermissionError:
        print("Error opening file")
        return
    except OSError:
        print("Error reading file")
        return

    change_by_month = monthly_change(jobs_data)

    print(yearly_change(change_by_month))

    # Get change by Presidential term
    change_by_president = {}
    names = list(presidents.keys())

    for name in names:
        change_by_president.update({name: new_jobs_by_pres(change_by_month, presidents, name)})

    jobs_democrats = new_jobs_by_party(change_by_president, presidents, 'D')
    jobs_republicans = new_jobs_by_party(change_by_president, presidents, 'R')

    print(f"Exhibit A: Total Jobs Produced by Party\n"
          f"Democrats: {format(jobs_democrats[0] * 1000, ',d')} Million\n"
          f"Republicans: {format(jobs_republicans[0] * 1000, ',d')} Million\n\n"
          f"Exhibit B: Average Jobs Produced by Party\n"
          f"Democrats: {format(int(jobs_democrats[1] * 1000), ',d')} Million\n"
          f"Republicans: {format(int(jobs_republicans[1] * 1000), ',d')} Million\n\n"
          "Exhibit C: Rendered Graph\n"
          "While Clinton's numbers were slightly different that what it shown by the data, they are relatively the \n"
          "same. As shown by the exhibit B and C, Democratic presidents, on average, produced\n"
          "more jobs in their terms than their Republican counterparts. According to the data, Clinton's assertion\n"
          "is correct. However, it is misleading as the polices put in place by one president will affect the next\n"
          "presidents term. Other external factors also must be taken into accounts, such as recessions. Bill Clinton\n"
          "by far had the highest job count of any president, but he inherited the \'dotcom\' boom. George Bush, on\n"
          "the other hand, experienced the the 2008 recession near the end of his presidency, skewing his\n"
          "numbers. Here are the number of job produced without 2008"
          )

    # plt_list = plt.bar(change_by_president.keys(), change_by_president.values(), width=0.4)
    # plt_list[2].set_color('red')
    # plt_list[3].set_color('red')
    # plt_list[5].set_color('red')
    # plt_list[6].set_color('red')
    # plt_list[8].set_color('red')
    # plt.xlabel("Presidents")
    # plt.ylabel("New Jobs")
    # plt.title("New Jobs by Presidential Terms")
    # plt.legend(handles=[plt.Rectangle((0, 0), 1, 1, color='red'), plt.Rectangle((0, 0), 1, 1, color='blue')],
    #            labels=['Republicans', 'Democrats'])
    # plt.show()

if __name__ == '__main__':
    main()

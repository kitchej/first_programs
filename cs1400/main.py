"""
Project Name: Project 7 - Was Clinton Right?
Author: Joshua Kitchen
Due Date: 12/7/2020
Course: CS1400-005
"""
import csv
from matplotlib import pyplot as plt


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
    return month_change_dict


# finds out change by year by adding the changes calculated in monthly_change()
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
    years = presidents_dict[president][1]
    for year in years:
        jobs += data[year]
    return jobs


def new_jobs_by_party(data, presidents_dict, party):
    jobs = 0
    for president in presidents_dict:
        if presidents_dict[president][0] == party:
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

    # {1961: [45119,44969,45051,44997,45119,45289,45400,45535,45591,45716,45931,46035}}
    jobs_data = {}
    for line in data:
        key = line.pop(0)
        jobs_data[key] = line

    # Get president info - 'John F. Kennedy': ('D', ['1961', '1962', '1963'])

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

    # Get change by year
    change_by_month = monthly_change(jobs_data)
    change_by_year = yearly_change(change_by_month)

    # Get change by Presidential term
    change_by_president = {}
    names = list(presidents.keys())

    for name in names:
        change_by_president.update({name: new_jobs_by_pres(change_by_year, presidents, name)})

    jobs_democrats = new_jobs_by_party(change_by_president, presidents, 'D')
    jobs_republicans = new_jobs_by_party(change_by_president, presidents, 'R')

    print(f"Exhibit A: Total Jobs Produced by Party\n"
          f"Democrats: {format(jobs_democrats[0] * 1000, ',d')} Million\n"
          f"Republicans: {format(jobs_republicans[0] * 1000, ',d')} Million\n\n"
          f"Exhibit B: Average Jobs Produced By Party Per Presidential Term\n"
          f"Democrats: {format(int(jobs_democrats[1] * 1000), ',d')} Million\n"
          f"Republicans: {format(int(jobs_republicans[1] * 1000), ',d')} Million\n\n"
          "Exhibit C: Rendered Graph\n\n"
          "As shown by the exhibit B and C, Democratic presidents, on average, saw more job increases\n"
          "in their terms than their Republican counterparts, with Bill Clinton seeing the most job growth.\n"
          "According to the data, Clinton's assertion appears correct. However, it is misleading as the polices put\n"
          "in place by one president will affect the next presidents term. Other external factors also must be taken\n"
          "into accounts, such as recessions. Even though Bill Clinton experienced the highest job count of any "
          "president,\n"
          "he inherited the \'dotcom\' boom and a thriving economy. George Bush, on the other hand, experienced the \n"
          "2008 recession near the end of his presidency."
          )

    # Shorten the names so they fit on the graph
    names = list(change_by_president.keys())
    last_names = []

    for name in names:
        if len(name.split()) == 2:
            last_names.append(name.split()[1])
        else:
            last_names.append(name.split()[2])

    last_names[8] = "W. Bush"

    plt_list = plt.bar(last_names, change_by_president.values(), width=0.4)
    plt_list[2].set_color('red')
    plt_list[3].set_color('red')
    plt_list[5].set_color('red')
    plt_list[6].set_color('red')
    plt_list[8].set_color('red')
    plt.xlabel("Presidents")
    plt.ylabel("New Jobs")
    plt.title("New Jobs by Presidential Terms")
    plt.legend(handles=[plt.Rectangle((0, 0), 1, 1, color='red'), plt.Rectangle((0, 0), 1, 1, color='blue')],
               labels=['Republicans', 'Democrats'])
    plt.show()


if __name__ == '__main__':
    main()

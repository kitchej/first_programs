"""
Project Name: Project 4 - Stock Exchange Data
Author: Joshua Kitchen
Due Date: 10/31/2020
Course: CS1400-005
"""
import csv
import os


def sort_stocks(stock_name, iterable):
    stocks = []
    for i in iterable:
        if i[0] == stock_name:
            stocks.append(i)
    return stocks


def sort_by_price(iterable, reverse=False):
    if reverse:
        return sorted(iterable, key=lambda item: float(item[2]), reverse=True)
    else:
        return sorted(iterable, key=lambda item: float(item[2]))


def find_average(iterable):
    total_price = 0.0
    for i in iterable:
        total_price += float(i[2])
    return total_price / len(iterable)


def main():

    filename = "stocks_data.csv"

    if not os.path.exists(filename):
        print(f"File \"{filename}\" does not exist")
        return

    with open(filename, 'r') as file:
        csv_reader = csv.reader(file)
        lines = []
        for line in csv_reader:
            lines.append(line)
        lines.pop(0)

    lowest_to_highest = sort_by_price(lines)

    highest_stock = lowest_to_highest[-1]
    lowest_stock = lowest_to_highest[0]

    ibm = sort_stocks('IBM', lines)
    ms = sort_stocks('MSFT', lines)
    apple = sort_stocks('AAPL', lines)

    ibm_lowest = sort_by_price(ibm)[0]
    apple_lowest = sort_by_price(apple)[0]
    ms_lowest = sort_by_price(ms)[0]

    ibm_highest = sort_by_price(ibm, reverse=True)[0]
    apple_highest = sort_by_price(apple, reverse=True)[0]
    ms_highest = sort_by_price(ms, reverse=True)[0]

    ibm_avg = find_average(ibm)
    apple_avg = find_average(apple)
    ms_avg = find_average(ms)

    stock_summary = f"{apple_highest[0]}\n"\
                    f"----\n"\
                    f"Max: {round(float(apple_highest[2]), 2)} {apple_highest[1]}\n"\
                    f"Min: {round(float(apple_lowest[2]), 2)} {apple_lowest[1]}\n"\
                    f"Ave: {round(float(apple_avg), 2)}\n\n"\
                    f"{ibm_highest[0]}\n"\
                    f"----\n"\
                    f"Max: {round(float(ibm_highest[2]), 2)} {ibm_highest[1]}\n"\
                    f"Min: {round(float(ibm_lowest[2]), 2)} {ibm_lowest[1]}\n"\
                    f"Ave: {round(float(ibm_avg), 2)}\n\n"\
                    f"{ms_highest[0]}\n"\
                    f"----\n"\
                    f"Max: {round(float(ms_highest[2]), 2)} {ms_highest[1]}\n"\
                    f"Min: {round(float(ms_lowest[2]), 2)} {ms_lowest[1]}\n"\
                    f"Ave: {round(float(ms_avg), 2)}\n\n"\
                    f"Highest: {highest_stock[0]} {round(float(highest_stock[2]), 2)} {highest_stock[1]}\n"\
                    f"Lowest: {lowest_stock[0]} {round(float(lowest_stock[2]), 2)} {lowest_stock[1]}"

    with open('stock_summary.txt', 'w') as file:
        file.write(stock_summary)

    print(stock_summary)


if __name__ == '__main__':
    main()

"""
DATA GENERATOR VERSION 2.0
WRITTEN BY JOSHUA KITCHEN - VERSION 1.0: Summer 2019; THIS VERSION: Jan 2020

This version is an overhaul of my Data Generator program. It had been awhile since I last looked at the code, and while
the code was fairly well organized, I realized it could be better. For example, the same code was being rewritten in
several different places, so I went through all the code and placed repeated code inside their own functions. This made
it much eaiser to update the code when needed. It also meant that more subprocess could call code without
needing to rewrite the same code over and over. This was critical as I continued to add more features to the program.

Other major changes:

- I changed the way files are saved. Now a folder called "Output" is made in the script's or exe's directory and
files are saved there. Instead of providing a full path, the user only has to specify a file name and extension. A
"settings()" function was added that allows the user to set their own default save directory.

- Since files were pretty much in csv format already, I changed the writing operations to use the csv module for better
support of the format.

TL;DR:
I revised the code, focusing on its optimization, clean up, and the potential for expansion.
 -----------------------------------------------------------------------------------------------------------

CATEGORIES AVAILABLE(version 2.0):
- DATES
    - Full dates in the following formats: month day, year; mm/dd/yyyy; day month year; dd/mm/yyyy
    - Months
    - Years
- NUMBERS
    - Integers
    - Floating point values
- NAMES
    - Only male first names
    - Only female first names
    - Only surnames
    - Mixed gender first names
    - Full male names
    - Full female names
    - Full mixed gender names
- DIE ROLLS (Up to six die)
- COIN TOSSES
- EMAILS
- ADDRESSES
    - Streets (only house numbers and street names)
    - Full (full address with house number, street, city, and state)
- PHONE NUMBERS
- STRINGS AND CHARACTERS
    - Any custom data provided by the user like city names, company names, characters, etc.
- TRUE/FALSE STATEMENTS
    - True or false statements such as "Is on probation," "Fees paid," "Is in the ICU," etc.
    - Returns "{your statement}: {True or False}
- RANDOM PEOPLE
    - Crates a list of generic people with:
        - A name (male, female, or mixed gender)
        - An address (optional)
        - An email (optional)
        - A phone number (optional)
- RANDOM STUDENTS
    - Creates a list of random students with:
        - A name (male, female, or mixed gender)
        - A GPA (optional)
        - A major (optional)
        - A class (freshman, sophomore, junior, senior; optional)
- RANDOM EMPLOYEES
    - Creates a list of random employees with:
        - A name (male, female, or mixed gender)
        - A salary (optional)
        - A position (optional)
        - Years worked (optional)
- CUSTOM DATA
    The custom data function allows for the user to create custom data sets, similar to the example sets RANDOM PEOPLE,
    RANDOM STUDENTS and RANDOM EMPLOYEES. The user will choose attributes for their data set by selecting any of the
    above functions to generate those attributes. The max is 6 attributes per object.
"""
import random
from datetime import datetime
import csv
import os
import re
from Date_data import months, months_to_num
from Names import names_males, names_females, surnames
from Student_data import majors, classes
from Employee_data import positions, salaries
from Address_data import streets, cities, states

# Global declarations that allow different functions to share data with each other when called within custom_data()
global att_1
global att_2
global att_3
global att_4
global att_5
global att_6


def show_categories():
    print("\ndates\nnames\nnumbers\ndie rolls\ncoin tosses\nemails\naddresses\nphone numbers\nstrings and characters\n"
          "true/false\nrandom people\nrandom students\nrandom employees\ncustom")


def dates(q=None, is_called_in_custom=False):
    if is_called_in_custom is True:
        pass
    while True:
        command = input("Options: full date, months, years\nEnter option: ")
        if command == "full date":
            while True:
                if q:
                    quantity = q
                else:
                    quantity = input("Quantity of dates(999 max): ")
                print("Enter range for the years. For dates in the same year, make the range start and end the same.")
                x = input("Range start: ")
                y = input("Range end: ")
                try:
                    random.randint(int(x), int(y))
                    int(quantity)
                    break
                except ValueError:
                    print("\nINVALID INPUT FOR RANGE OR QUANTITY. Note: \"range start\" must be less than "
                          "\"range end.\"\n")
            form = input("Choose date format \na: month day, year; b: mm/dd/yyyy; c: day month year; d: dd/mm/yyyy: ")
            if form == "a":
                rand_dates = []
                for i in range(int(quantity)):
                    year = random.randint(int(x), int(y))
                    month = random.choice(months)
                    if month == ("January", "March", "May", "July", "August", "October", "December"):
                        day = random.randint(1, 31)
                    elif month == "February":
                        if (year % 400 == 0) or (year % 4 == 0) and (year % 100 != 0):
                            day = random.randint(1, 29)
                        else:
                            day = random.randint(1, 28)
                    else:
                        day = random.randint(1, 30)
                    rand_dates.append(f"{month} {day}, {year}")
                while True:
                    sort_option = input("Sort rand_dates? Options: sort ascending, sort descending, no sort: ")
                    if sort_option == "sort ascending":
                        rand_dates.sort(key=lambda date_sort: datetime.strptime(date_sort, '%B %d; %Y'))
                        return rand_dates
                    elif sort_option == "sort descending":
                        rand_dates.sort(reverse=True, key=lambda date_sort: datetime.strptime(date_sort, '%B %d; %Y'))
                        return rand_dates
                    elif sort_option == "no sort":
                        return rand_dates
                    else:
                        print(f"\n\"{sort_option}\" IS NOT A VALID INPUT\n")
            elif form == "b":
                rand_dates = []
                for i in range(int(quantity)):
                    month = random.choice(months)
                    numerical_month = months_to_num[month]
                    year = random.randint(int(x), int(y))
                    if month == ("January", "March", "May", "July", "August", "October", "December"):
                        day = random.randint(1, 31)
                    elif month == "February":
                        if (year % 400 == 0) or (year % 4 == 0) and (year % 100 != 0):
                            day = random.randint(1, 29)
                        else:
                            day = random.randint(1, 28)
                    else:
                        day = random.randint(1, 30)
                    rand_dates.append(f"{numerical_month}/{day}/{year}")
                while True:
                    sort_option = input("Sort rand_dates? Options: sort ascending, sort descending, no sort: ")
                    if sort_option == "sort ascending":
                        rand_dates.sort(key=lambda date_sort: datetime.strptime(date_sort, '%m/%d/%Y'))
                        return rand_dates
                    elif sort_option == "sort descending":
                        rand_dates.sort(reverse=True, key=lambda date_sort: datetime.strptime(date_sort, '%m/%d/%Y'))
                        return rand_dates
                    elif sort_option == "no sort":
                        return rand_dates
                    else:
                        print(f"\n\"{sort_option}\" IS NOT A VALID INPUT\n")
            elif form == "c":
                rand_dates = []
                for i in range(int(quantity)):
                    month = random.choice(months)
                    year = random.randint(int(x), int(y))
                    if month == ("January", "March", "May", "July", "August", "October", "December"):
                        day = random.randint(1, 31)
                    elif month == "February":
                        if (year % 400 == 0) or (year % 4 == 0) and (year % 100 != 0):
                            day = random.randint(1, 29)
                        else:
                            day = random.randint(1, 28)
                    else:
                        day = random.randint(1, 30)
                    rand_dates.append(f"{day} {month} {year}")
                while True:
                    sort_option = input("Sort rand_dates? Options: sort ascending, sort descending, no sort: ")
                    if sort_option == "sort ascending":
                        rand_dates.sort(key=lambda date_sort: datetime.strptime(date_sort, '%d %B %Y'))
                        return rand_dates
                    elif sort_option == "sort descending":
                        rand_dates.sort(reverse=True, key=lambda date_sort: datetime.strptime(date_sort, '%d %B %Y'))
                        return rand_dates
                    elif sort_option == "no sort":
                        return rand_dates
                    else:
                        print(f"\n\"{sort_option}\" IS NOT A VALID INPUT\n")
            elif form == "d":
                rand_dates = []
                for i in range(int(quantity)):
                    month = random.choice(months)
                    numerical_month = months_to_num[month]
                    year = random.randint(int(x), int(y))
                    if month == ("January", "March", "May", "July", "August", "October", "December"):
                        day = random.randint(1, 31)
                    elif month == "February":
                        if (year % 400 == 0) or (year % 4 == 0) and (year % 100 != 0):
                            day = random.randint(1, 29)
                        else:
                            day = random.randint(1, 28)
                    else:
                        day = random.randint(1, 30)
                    rand_dates.append(f"{day}/{numerical_month}/{year}")
                    while True:
                        sort_option = input("Sort rand_dates? Options: sort ascending, sort descending, no sort: ")
                        if sort_option == "sort ascending":
                            rand_dates.sort(key=lambda date_sort: datetime.strptime(date_sort, '%d/%m/%Y'))
                            return rand_dates
                        elif sort_option == "sort descending":
                            rand_dates.sort(
                                reverse=True, key=lambda date_sort: datetime.strptime(date_sort, '%d/%m/%Y')
                            )
                            return rand_dates
                        elif sort_option == "no sort":
                            return rand_dates
                        else:
                            print(f"\n\"{sort_option}\" IS NOT A VALID INPUT\n")
                else:
                    print(f"\n\"{form}\" IS NOT A VALID INPUT\n")
                    break
        elif command == "months":
            rand_month = []
            while True:
                if q:
                    quantity = q
                else:
                    quantity = input("Quantity of rand_dates(999 max): ")
                try:
                    int(quantity)
                    break
                except ValueError:
                    print("INVALID INPUT FOR QUANTITY")
            for i in range(int(quantity)):
                rand_month.append(random.choice(months))
            return rand_month
        elif command == "years":
            while True:
                if q:
                    quantity = q
                    x = input("Range start: ")
                    y = input("Range end: ")
                else:
                    quantity = input("Quantity of rand_dates(999 max): ")
                    x = input("Range start: ")
                    y = input("Range end: ")
                try:
                    random.randint(int(x), int(y))
                    int(quantity)
                    break
                except ValueError:
                    print("\nINVALID INPUT FOR RANGE OR QUANTITY. Note: \"range start\" must be less than "
                          "\"range end.\"\n")
            rand_year = []
            for i in range(int(quantity)):
                rand_year.append(random.randint(int(x), int(y)))
            return rand_year
        else:
            print(f"\n\"{command}\" IS NOT A VALID INPUT\n")


def names(q=None, is_called_in_custom=False):
    while True:
        command = input("Categories: names male, names female, mixed, surnames, full names male, full names female, "
                        "full names mixed\nEnter category: ")
        if command == "names male":
            while True:
                if q:
                    quantity = q
                else:
                    quantity = input("Quantity of names(999 max): ")
                try:
                    if int(quantity) <= 999:
                        break
                    else:
                        print("\nQUANTITY IS TOO LARGE")
                except ValueError:
                    print("\nINVALID INPUT FOR QUANTITY")
            rand_name_males = random.sample(names_males, k=int(quantity))
            if is_called_in_custom is True:
                rand_name_males.insert(0, "names")
            return rand_name_males
        elif command == "names female":
            while True:
                if q:
                    quantity = q
                else:
                    quantity = input("Quantity of names(999 max): ")
                try:
                    if int(quantity) <= 999:
                        break
                    else:
                        print("\nQUANTITY IS TOO LARGE")
                except ValueError:
                    print("\nINVALID INPUT FOR QUANTITY")
            rand_name_females = random.sample(names_females, k=int(quantity))
            if is_called_in_custom is True:
                rand_name_females.insert(0, "names")
            return rand_name_females
        elif command == "mixed":
            while True:
                if q:
                    quantity = q
                else:
                    quantity = input("Quantity of names(999 max): ")
                try:
                    if int(quantity) <= 999:
                        break
                    else:
                        print("\nQUANTITY IS TOO LARGE")
                except ValueError:
                    print("\nINVALID INPUT FOR QUANTITY")
            mixed_names = []
            if is_called_in_custom is True:
                mixed_names.append("names")
            rand_name_females = random.sample(names_females, k=int(quantity))
            rand_name_males = random.sample(names_males, k=int(quantity))
            for i in range(int(quantity)):
                z = random.randint(0, 1)
                if z == 0:
                    mixed_names.append(rand_name_females[i])
                else:
                    mixed_names.append(rand_name_males[i])
            return mixed_names
        elif command == "surnames":
            while True:
                if q:
                    quantity = q
                else:
                    quantity = input("Quantity of names(999 max): ")
                try:
                    if int(quantity) <= 999:
                        break
                    else:
                        print("\nQUANTITY IS TOO LARGE")
                except ValueError:
                    print("\nINVALID INPUT FOR QUANTITY")
            rand_name_surname = random.sample(surnames, k=int(quantity))
            if is_called_in_custom is True:
                rand_name_surname.insert(0, "names")
            return rand_name_surname
        elif command == "full names male":
            while True:
                if q:
                    quantity = q
                else:
                    quantity = input("Quantity of names(999 max): ")
                try:
                    if int(quantity) <= 999:
                        break
                    else:
                        print("\nQUANTITY IS TOO LARGE")
                except ValueError:
                    print("\nINVALID INPUT FOR QUANTITY")
            rand_names_first = random.sample(names_males, k=int(quantity))
            rand_names_last = random.sample(surnames, k=int(quantity))
            full_names_male = []
            if is_called_in_custom is True:
                full_names_male.append("names")
            for i in range(int(quantity)):
                full_names_male.append(f"{rand_names_first[i]} {rand_names_last[i]}")
            return full_names_male
        elif command == "full names female":
            while True:
                if q:
                    quantity = q
                else:
                    quantity = input("Quantity of names(999 max): ")
                try:
                    if int(quantity) <= 999:
                        break
                    else:
                        print("\nQUANTITY IS TOO LARGE")
                except ValueError:
                    print("\nINVALID INPUT FOR QUANTITY")
            rand_names_first = random.sample(names_females, k=int(quantity))
            rand_names_last = random.sample(surnames, k=int(quantity))
            full_names_female = []
            if is_called_in_custom is True:
                full_names_female.append("names")
            for i in range(int(quantity)):
                full_names_female.append(f"{rand_names_first[i]} {rand_names_last[i]}")
            return full_names_female
        elif command == "full names mixed":
            while True:
                if q:
                    quantity = q
                else:
                    quantity = input("Quantity of names(999 max): ")
                try:
                    if int(quantity) <= 999:
                        break
                    else:
                        print("\nQUANTITY IS TOO LARGE")
                except ValueError:
                    print("\nINVALID INPUT FOR QUANTITY")
            rand_names_first_f = random.sample(names_females, k=int(quantity))
            rand_names_first_m = random.sample(names_males, k=int(quantity))
            rand_names_last = random.sample(surnames, k=int(quantity))
            mixed_full_names = []
            if is_called_in_custom is True:
                mixed_full_names.append("names")
            for i in range(int(quantity)):
                z = random.randint(0, 1)
                if z == 0:
                    first = rand_names_first_f[i]
                else:
                    first = rand_names_first_m[i]
                mixed_full_names.append(f"{first} {rand_names_last[i]}")
            return mixed_full_names
        else:
            print(f"\"{command}\" IS NOT A VALID INPUT")


def numbers(q=None, is_called_in_custom=False):
    if is_called_in_custom is True:
        pass
    while True:
        command = input("For whole numbers only, type \"integers\", otherwise press enter to continue: ")
        if command == "integers":
            integers = []
            while True:
                if q:
                    quantity = q
                else:
                    quantity = input("Quantity of numbers desired: ")
                x = input("Range start: ")
                y = input("Range end: ")
                try:
                    random.randint(int(x), int(y))
                    int(quantity)
                    break
                except ValueError:
                    print("INVALID INPUT FOR RANGE. Note: \"range start\" must be less than \"range end.\"")
            for _ in range(int(quantity)):
                integers.append(f"{random.randint(int(x), int(y))}")
            return integers
        elif command == "":
            floats = []
            while True:
                if q:
                    quantity = q
                else:
                    quantity = input("Quantity of numbers desired: ")
                x = input("Range start: ")
                y = input("Range end: ")
                r = input("Number of decimal places to round to: ")
                try:
                    random.randint(int(x), int(y))
                    int(r)
                    int(quantity)
                    break
                except ValueError:
                    print("INVALID INPUT FOR RANGE. Note: \"range start\" must be less than \"range end.\"")
            for _ in range(int(quantity)):
                num = random.uniform(int(x), int(y))
                floats.append(f"{round(num, int(r))}")
            return floats
        else:
            print(f"\"{command}\" IS NOT A VALID INPUT")


def die_rolls(q=None, is_called_in_custom=False):
    if is_called_in_custom is True:
        pass
    results = []
    while True:
        command = input("Input number of die (1-6): ")
        while True:
            if q:
                quantity = q
            else:
                quantity = input("Quantity of rolls: ")
            try:
                int(quantity)
                break
            except ValueError:
                print("\nINVALID INPUT FOR QUANTITY")
        if command == "1":
            for i in range(int(quantity)):
                results.append([f"Set{i + 1}: ", random.randint(1, 6)])
            return results
        elif command == "2":
            for i in range(int(quantity)):
                results.append([f"Set {i + 1}: ", random.randint(1, 6), random.randint(1, 6)])
            return results
        elif command == "3":
            for i in range(int(quantity)):
                results.append([f"Set {i + 1}:", random.randint(1, 6), random.randint(1, 6), random.randint(1, 6)])
            return results
        elif command == "4":
            for i in range(int(quantity)):
                results.append([f"Set {i + 1}:", random.randint(1, 6), random.randint(1, 6), random.randint(1, 6),
                                random.randint(1, 6)])
            return results
        elif command == "5":
            for i in range(int(quantity)):
                results.append([f"Set {i + 1}:", random.randint(1, 6), random.randint(1, 6), random.randint(1, 6),
                                random.randint(1, 6), random.randint(1, 6)])
            return results
        elif command == "6":
            for i in range(int(quantity)):
                results.append([f"Set {i + 1}:", random.randint(1, 6), random.randint(1, 6), random.randint(1, 6),
                                random.randint(1, 6), random.randint(1, 6), random.randint(1, 6)])
            return results
        elif command == "back":
            break
        else:
            print(f"\"{command}\" IS NOT A VALID INPUT")


def coin_tosses(q=None, is_called_in_custom=False):
    if is_called_in_custom is True:
        pass
    total_tosses = []
    while True:
        if q:
            quantity = q
        else:
            quantity = input("Quantity of tosses: ")
        try:
            int(quantity)
            break
        except ValueError:
            print("\nINVALID INPUT FOR QUANTITY")
    for i in range(int(quantity)):
        toss = random.randint(0, 1)
        if toss == 0:
            total_tosses.append("Heads")
        else:
            total_tosses.append("Tails")
    return total_tosses


def emails(q=None, is_called_in_custom=False):
    total_emails = []
    domains = ["gmail.com", "yahoo.com", "hotmail.com", "aol.com"]
    while True:
        if q:
            quantity = q
        else:
            quantity = input("Quantity of emails(999 max): ")
        try:
            if int(quantity) <= 999:
                break
            else:
                print("\nQUANTITY IS TOO LARGE")
        except ValueError:
            print("\nINVALID INPUT FOR QUANTITY")
    if is_called_in_custom is True:
        email_name_bank = []
        if att_1[0] == "names":
            att_1.remove("names")
            email_name_bank = att_1
        elif att_2[0] == "names":
            att_2.remove("names")
            email_name_bank = att_2
        elif att_3[0] == "names":
            att_3.remove("names")
            email_name_bank = att_3
        elif att_4[0] == "names":
            att_4.remove("names")
            email_name_bank = att_4
        elif att_5[0] == "names":
            att_5.remove("names")
            email_name_bank = att_5
        elif att_6[0] == "names":
            att_6.remove("names")
            email_name_bank = att_6
        if len(email_name_bank[0].split(" ")) == 2:
            for name in email_name_bank:
                email_name = name.split()
                var = random.randint(0, 1)
                if var == 0:
                    var_1 = random.randint(0, 1)
                    if var_1 == 0:
                        total_emails.append(f"{(email_name[0].lower()).strip()}.{(email_name[1].lower()).strip()}"
                                            f"@{random.choice(domains)}")
                    else:
                        total_emails.append(f"{(email_name[1].lower()).strip()}.{(email_name[0].lower()).strip()}"
                                            f"@{random.choice(domains)}")
                else:
                    total_emails.append(f"{(email_name[0].lower()).strip()}.{(email_name[0][0]).strip()}"
                                        f"{random.randint(100, 9999)}@{random.choice(domains)}")
        else:
            for name in email_name_bank:
                var = random.randint(0, 1)
                if var == 0:
                    total_emails.append(f"{(name.lower()).strip()}{random.randint(100, 9999)}@{random.choice(domains)}")
                else:
                    total_emails.append(f"{random.randint(100, 9999)}{(name.lower()).strip()}@{random.choice(domains)}")
        return total_emails
    else:
        for i in range(int(quantity)):
            var = random.randint(0, 1)
            if var == 0:
                name_var = random.randint(0, 1)
                if name_var == 0:
                    first = random.choice(names_males)
                else:
                    first = random.choice(names_females)
                last = random.choice(surnames)
                var_1 = random.randint(0, 1)
                if var_1 == 0:
                    total_emails.append(f"{first.lower()}.{last.lower()}@{random.choice(domains)}")
                else:
                    total_emails.append(f"{last.lower()}.{first.lower()}@{random.choice(domains)}")
            elif var == 1:
                name_var = random.randint(0, 1)
                if name_var == 0:
                    first = random.choice(names_males)
                else:
                    first = random.choice(names_females)
                last = random.choice(surnames)
                total_emails.append(f"{first.lower()}{last[0]}{random.randint(100, 9999)}"
                                    f"@{random.choice(domains)}")
            else:
                name_var = random.randint(0, 1)
                if name_var == 0:
                    first = random.choice(names_males)
                else:
                    first = random.choice(names_females)
                var_2 = random.randint(0, 1)
                if var_2 == 0:
                    total_emails.append(f"{first.lower()}.{random.randint(100, 9999)}@{random.choice(domains)}")
                else:
                    total_emails.append(f"{random.randint(100, 9999)}.{first.lower()}@{random.choice(domains)}")
        return total_emails


def addresses(q=None, is_called_in_custom=False):
    if is_called_in_custom is True:
        pass
    rand_addresses = []
    while True:
        command = input("Options - \"street\"(just the house number and street) or \"full\"(full address with house "
                        "number, street, city, and state): ")

        if command == "street":
            while True:
                if q:
                    quantity = q
                else:
                    quantity = input("Quantity of rand_addresses(999 max): ")
                try:
                    if int(quantity) <= 999:
                        break
                    else:
                        print("\nQUANTITY IS TOO LARGE")
                except ValueError:
                    print("\nINVALID INPUT FOR QUANTITY")
            street = random.sample(streets, k=int(quantity))
            for i in range(int(quantity)):
                rand_addresses.append(f"{random.randint(1, 9999)} {street[i]}")
            return rand_addresses
        elif command == "full":
            while True:
                if q:
                    quantity = q
                else:
                    quantity = input("Quantity of rand_addresses(999 max): ")
                try:
                    if int(quantity) <= 999:
                        break
                    else:
                        print("\nQUANTITY IS TOO LARGE")
                except ValueError:
                    print("\nINVALID INPUT FOR QUANTITY")
            street = random.sample(streets, k=int(quantity))
            city = random.sample(cities, k=int(quantity))
            state = random.choices(states, k=int(quantity))
            for i in range(int(quantity)):
                rand_addresses.append(f"{ random.randint(1, 9999)} {street[i]}, {city[i]}, {state[i]}")
            return rand_addresses
        else:
            print(f"\"{command}\" IS NOT A VALID OPTION")


def phone_num(q=None, is_called_in_custom=False):
    if is_called_in_custom is True:
        pass
    phone_numbers = []
    while True:
        if q:
            quantity = q
        else:
            quantity = input("Quantity of phone numbers: ")
        try:
            int(quantity)
            break
        except ValueError:
            print("\nINVALID INPUT FOR QUANTITY")
    for i in range(int(quantity)):
        phone_numbers.append(f"{random.randint(100,999)}-{random.randint(100, 999)}-{random.randint(1000, 9999)}")
    return phone_numbers


def boolean(q=None, is_called_in_custom=False):
    output_bool = []
    if is_called_in_custom is True:
        while True:
            if q:
                quantity = q
            else:
                quantity = input("Quantity of statements(999 max): ")
            try:
                int(quantity)
                break
            except ValueError:
                print("\nINVALID INPUT FOR QUANTITY")
        for i in range(int(quantity)):
            n = random.randint(0, 1)
            if n == 0:
                output_bool.append("True")
            else:
                output_bool.append("False")
    else:
        print("Enter a true/false statement\nExample: \"Is on probation\", \"Is in the ICU\", \"Fees paid\"")
        statement = input("Statement: ")
        while True:
            if q:
                quantity = q
            else:
                quantity = input("Quantity of statements(999 max): ")
            try:
                int(quantity)
                break
            except ValueError:
                print("\nINVALID INPUT FOR QUANTITY")
        for i in range(int(quantity)):
            n = random.randint(0, 1)
            if n == 0:
                output_bool.append([f"{statement}:", "True"])
            else:
                output_bool.append([f"{statement}:", "False"])
        return output_bool


def string_and_char(q=None, is_called_in_custom=False):
    if is_called_in_custom is True:
        pass
    while True:
        command = input("To use custom data, type \"custom\". To quickly create a list of "
                        "values to use, type \"quick custom\": ")
        if command == "custom":
            data_name = input("Enter file path to data bank: ")
            try:
                with open(data_name, "r") as data_file:
                    data_bank = data_file.read()
                data = data_bank.split(", ")
                break
            except PermissionError:
                print("CANNOT ACCESS FILE")
            except FileNotFoundError:
                print("FILE PATH NOT FOUND")
            except OSError:
                print("CANNOT SAVE FILE")
            except ValueError:
                print("INVALID INPUT")
        elif command == "quick custom":
            user_list = input("Enter values. After entering a value, separate it by a comma and a space except for the "
                              "last value.\nExample: a, b, c, d, e: ")
            data = user_list.split(", ")
            break
        else:
            print(f"\"{command}\" IS NOT A VALID INPUT")
    while True:
        sample = input("Type \"choices\" to randomly choose data (Duplicated values possible). Type \"sample\" to "
                       "get a sample of data (No duplicate values): ")
        if sample == "choices":
            while True:
                if q:
                    quantity = q
                else:
                    quantity = input(F"Quantity of values desired (MAX: {len(data)}): ")
                try:
                    int(quantity)
                    break
                except ValueError:
                    print("INVALID INPUT FOR QUANTITY")
            values = random.choices(data, k=int(quantity))
            break
        elif sample == "sample":
            while True:
                if q:
                    quantity = q
                else:
                    quantity = input(F"Quantity of values desired (MAX: {len(data)}): ")
                try:
                    int(quantity)
                    break
                except ValueError:
                    print("INVALID INPUT FOR QUANTITY")
            values = random.sample(data, k=int(quantity))
            break
        else:
            print(f"\"{sample}\" IS NOT A VALID INPUT")
    while True:
        sort_option = input("Sort data in alphabetical order? Options: sort ascending, sort descending, no sort: ")
        if sort_option == "sort ascending":
            values.sort()
            return values
        elif sort_option == "sort descending":
            values.sort(reverse=True)
            return values
        elif sort_option == "no sort":
            return values
        else:
            print(f"\"{sort_option}\" IS NOT A VALID INPUT")


def random_people():
    people_names = []
    people_addresses = []
    people_emails = []
    people_numbers = []
    while True:
        quantity = input("First, enter quantity of people(999 MAX): ")
        try:
            if int(quantity) <= 999:
                break
            else:
                print("\nQUANTITY IS TOO LARGE")
        except ValueError:
            print("\nINVALID INPUT FOR QUANTITY")
    while True:
        name_type = input("Next, enter the type of names you want\nOptions: a. Male names only, "
                          "b. Female names only c. Mixed: ")
        if name_type == "a":
            rand_names_first_m = random.sample(names_males, k=int(quantity))
            rand_names_last = random.sample(surnames, k=int(quantity))
            for i in range(int(quantity)):
                people_names.append(f"{rand_names_first_m[i]}  {rand_names_last[i]}")
            break
        elif name_type == "b":
            rand_names_first_f = random.sample(names_females, k=int(quantity))
            rand_names_last = random.sample(surnames, k=int(quantity))
            for i in range(int(quantity)):
                people_names.append(f"{rand_names_first_f[i]}  {rand_names_last[i]}")
            break
        elif name_type == "c":
            rand_names_first_f = random.sample(names_females, k=int(quantity))
            rand_names_first_m = random.sample(names_males, k=int(quantity))
            rand_names_last = random.sample(surnames, k=int(quantity))
            for i in range(int(quantity)):
                z = random.randint(0, 1)
                if z == 0:
                    first = rand_names_first_f[i]
                else:
                    first = rand_names_first_m[i]
                last = rand_names_last[i]
                people_names.append(f"{first} {last}")
            break
        else:
            print(f"\"{name_type}\" IS NOT A VALID INPUT")
    print("Now select some options")
    while True:
        option_1 = input("Will the people have an address? y/n: ")
        if option_1 == "y":
            while True:
                sub_option_1 = input("Type \"street\" for just a street address or \"full\" for a full address "
                                     "(street address + city and state): ")
                if sub_option_1 == "street":
                    street = random.sample(streets, k=int(quantity))
                    for i in range(int(quantity)):
                        people_addresses.append(f"{random.randint(1, 9999)} {street[i]}")
                    break
                elif sub_option_1 == "full":
                    street = random.sample(streets, k=int(quantity))
                    city = random.sample(cities, k=int(quantity))
                    for i in range(int(quantity)):
                        people_addresses.append(f"{random.randint(1, 9999)} {street[i]}, {city[i]}, "
                                                f"{random.choice(states)}")
                    break
                else:
                    print(f"\"{sub_option_1}\" IS NOT A VALID INPUT")
            break
        elif option_1 == "n":
            break
        else:
            print(f"\"{option_1}\" IS NOT A VALID INPUT")
    while True:
        option_2 = input("Will people have an email? y/n: ")
        if option_2 == "y":
            domains = ["gmail.com", "yahoo.com", "hotmail.com", "aol.com"]
            for name in people_names:
                s = name.split()
                var = random.randint(0, 2)
                if var == 0:
                    try:
                        var_1 = random.randint(0, 1)
                        if var_1 == 0:
                            people_emails.append(f"{s[0].lower()}.{s[1].lower()}@{random.choice(domains)}")
                        else:
                            people_emails.append(f"{s[1].lower()}.{s[0].lower()}@{random.choice(domains)}")
                    except IndexError:
                        people_emails.append(f"{s[0].lower()}{random.randint(100, 9999)}"
                                             f"@{random.choice(domains)}")
                elif var == 1:
                    try:
                        var_2 = random.randint(0, 1)
                        if var_2 == 0:
                            people_emails.append(
                                f"{s[0].lower()}{s[1][0]}{random.randint(100, 9999)}"
                                f"@{random.choice(domains)}")
                        else:
                            people_emails.append(
                                f"{s[1][0]}{s[0].lower()}{random.randint(100, 9999)}"
                                f"@{random.choice(domains)}")
                    except IndexError:
                        people_emails.append(f"{s[0].lower()}{random.randint(100, 9999)}"
                                             f"@{random.choice(domains)}")
                else:
                    people_emails.append(f"{s[0].lower()}{random.randint(100, 9999)}"
                                         f"@{random.choice(domains)}")
            break
        elif option_2 == "n":
            break
        else:
            print(f"\"{option_2}\" IS NOT A VALID INPUT")
    while True:
        option_3 = input("Will people have a phone number? y/n: ")
        if option_3 == "y":
            for i in range(int(quantity)):
                people_numbers.append(f"{random.randint(100,999)}-{random.randint(100, 999)}"
                                      f"-{random.randint(1000, 9999)}")
            break
        elif option_3 == "n":
            break
        else:
            print(f"\"{option_3}\" IS NOT A VALID INPUT")
    people = []
    if people_names:
        for name in people_names:
            people.append([name])
    else:
        pass
    if people_addresses:
        i = 0
        for person in people:
            person.append(people_addresses[i])
            i += 1
    else:
        pass
    if people_emails:
        i = 0
        for person in people:
            person.append(people_emails[i])
            i += 1
    else:
        pass
    if people_numbers:
        i = 0
        for person in people:
            person.append(people_numbers[i])
            i += 1
    else:
        pass
    return people


def random_students():
    student_names = []
    student_gpa = []
    student_majors = []
    student_class = []
    while True:
        quantity = input("First, enter quantity of students(999 MAX): ")
        try:
            if int(quantity) <= 999:
                break
            else:
                print("\nQUANTITY IS TOO LARGE")
        except ValueError:
            print("\nINVALID INPUT FOR QUANTITY")
    while True:
        path_student = input("Enter file path_student to write data to. The only file extension supported in "
                             "this version is .csv: ")
        if ".csv" in path_student:
            break
        else:
            print("\nFILE NAME DOES NOT HAVE A FILE EXTENSION OR INVALID FILE EXTENSION")
    while True:
        name_type = input("Next, enter the type of names for your students\nOptions: a. Male names only, "
                          "b. Female names only c. Mixed: ")
        if name_type == "a":
            rand_names_first_m = random.sample(names_males, k=int(quantity))
            rand_names_last = random.sample(surnames, k=int(quantity))
            for i in range(int(quantity)):
                student_names.append(f"{rand_names_first_m[i]}  {rand_names_last[i]}")
            break
        elif name_type == "b":
            rand_names_first_f = random.sample(names_females, k=int(quantity))
            rand_names_last = random.sample(surnames, k=int(quantity))
            for i in range(int(quantity)):
                student_names.append(f"{rand_names_first_f[i]}  {rand_names_last[i]}")
            break
        elif name_type == "c":
            rand_names_first_f = random.sample(names_females, k=int(quantity))
            rand_names_first_m = random.sample(names_males, k=int(quantity))
            rand_names_last = random.sample(surnames, k=int(quantity))
            for i in range(int(quantity)):
                z = random.randint(0, 1)
                if z == 0:
                    first = rand_names_first_f[i]
                else:
                    first = rand_names_first_m[i]
                last = rand_names_last[i]
                student_names.append(f"{first} {last}")
            break
        else:
            print(f"\"{name_type}\" IS NOT A VALID INPUT")
    print("Now select some options")
    while True:
        option_1 = input("Will the student have a GPA? y/n: ")
        if option_1 == "y":
            for i in range(int(quantity)):
                student_gpa.append(round(random.uniform(2.0, 4.0), 2))
            break
        elif option_1 == "n":
            break
        else:
            print(f"\"{option_1}\" IS NOT A VALID INPUT")
    while True:
        option_2 = input("Will student have a major? y/n: ")
        if option_2 == "y":
            for i in range(int(quantity)):
                student_majors.append(random.choice(majors))
            break
        elif option_2 == "n":
            break
        else:
            print(f"\"{option_2}\" IS NOT A VALID INPUT")
    while True:
        option_3 = input("Will student have a class? y/n: ")
        if option_3 == "y":
            for i in range(int(quantity)):
                student_class.append(random.choice(classes))
            break
        elif option_3 == "n":
            break
        else:
            print(f"\"{option_3}\" IS NOT A VALID INPUT")
    students = []
    if student_names:
        for student in student_names:
            students.append([student])
    else:
        pass
    if student_gpa:
        i = 0
        for student in students:
            student.append(student_gpa[i])
            i += 1
    else:
        pass
    if student_majors:
        i = 0
        for student in students:
            student.append(student_majors[i])
            i += 1
    else:
        pass
    if student_class:
        i = 0
        for student in students:
            student.append(student_class[i])
            i += 1
    else:
        pass
    return students


def random_employees():
    employee_names = []
    employee_salary = []
    employee_position = []
    employee_years_worked = []
    while True:
        quantity = input("First, enter quantity of employees(999 MAX): ")
        try:
            if int(quantity) <= 999:
                break
            else:
                print("\nQUANTITY IS TOO LARGE")
        except ValueError:
            print("\nINVALID INPUT FOR QUANTITY")
    while True:
        path_employee = input("Enter file path to write data to. The only file extension supported in "
                              "this version is .csv: ")
        if ".csv" in path_employee:
            break
        else:
            print("\nFILE NAME DOES NOT HAVE A FILE EXTENSION OR INVALID FILE EXTENSION")
    while True:
        name_type = input("Next, enter the type of names for your employees\nOptions: a. Male names only, "
                          "b. Female names only c. Mixed: ")
        if name_type == "a":
            rand_names_first_m = random.sample(names_males, k=int(quantity))
            rand_names_last = random.sample(surnames, k=int(quantity))
            for i in range(int(quantity)):
                employee_names.append(f"{rand_names_first_m[i]}  {rand_names_last[i]}")
            break
        elif name_type == "b":
            rand_names_first_f = random.sample(names_females, k=int(quantity))
            rand_names_last = random.sample(surnames, k=int(quantity))
            for i in range(int(quantity)):
                employee_names.append(f"{rand_names_first_f[i]}  {rand_names_last[i]}")
            break
        elif name_type == "c":
            rand_names_first_f = random.sample(names_females, k=int(quantity))
            rand_names_first_m = random.sample(names_males, k=int(quantity))
            rand_names_last = random.sample(surnames, k=int(quantity))
            for i in range(int(quantity)):
                z = random.randint(0, 1)
                if z == 0:
                    first = rand_names_first_f[i]
                else:
                    first = rand_names_first_m[i]
                last = rand_names_last[i]
                employee_names.append(f"{first} {last}")
            break
        else:
            print(f"\"{name_type}\" IS NOT A VALID INPUT")
    print("Now select some options")
    while True:
        option_1 = input("Will the employee have a salary? y/n: ")
        if option_1 == "y":
            for i in range(int(quantity)):
                employee_salary.append(random.choice(salaries))
            break
        elif option_1 == "n":
            break
        else:
            print(f"\"{option_1}\" IS NOT A VALID INPUT")
    while True:
        option_2 = input("Will employee have a position? y/n: ")
        if option_2 == "y":
            for i in range(int(quantity)):
                employee_position.append(random.choice(positions))
            break
        elif option_2 == "n":
            break
        else:
            print(f"\"{option_2}\" IS NOT A VALID INPUT")
    while True:
        option_3 = input("Will employee have years worked? y/n: ")
        if option_3 == "y":
            for i in range(int(quantity)):
                employee_years_worked.append(random.randint(1, 30))
            break
        elif option_3 == "n":
            break
        else:
            print(f"\"{option_3}\" IS NOT A VALID INPUT")
    employees = []
    if employee_names:
        for employee in employee_names:
            employees.append([employee])
    else:
        pass
    if employee_salary:
        i = 0
        for employee in employees:
            employee.append(employee_salary[i])
            i += 1
    else:
        pass
    if employee_position:
        i = 0
        for employee in employees:
            employee.append(employee_position[i])
            i += 1
    else:
        pass
    if employee_years_worked:
        i = 0
        for employee in employees:
            employee.append(employee_years_worked[i])
            i += 1
    else:
        pass
    return employees


def custom_data():
    while True:
        quantity = input("Quantity of sets desired (MAX 999): ")
        try:
            if int(quantity) <= 999:
                break
            else:
                print("\nQUANTITY IS TOO LARGE")
        except ValueError:
            print("\nINVALID INPUT FOR QUANTITY")
    print("\nChoose what type of data each attribute will be. The max is six. If an attribute slot will not be "
          "used, press \"enter\"")
    funcs = {
        "dates": dates,
        "names": names,
        "numbers": numbers,
        "emails": emails,
        "addresses": addresses,
        "phone numbers": phone_num,
        "string/char": string_and_char,
        "true/false": boolean
        }
    global att_1
    global att_2
    global att_3
    global att_4
    global att_5
    global att_6
    att_1 = []
    att_2 = []
    att_3 = []
    att_4 = []
    att_5 = []
    att_6 = []
    choice_1 = None
    choice_2 = None
    choice_3 = None
    choice_4 = None
    choice_5 = None
    choice_6 = None
    labels = []
    total = []
    while True:
        lab_1 = input("\nEnter label for attribute 1: ")
        if lab_1 == "":
            pass
        else:
            while True:
                choice_1 = input("Enter attribute type for choice 1: ")
                try:
                    labels.append(lab_1)
                    att_1 = funcs[choice_1](q=int(quantity), is_called_in_custom=True)
                    break
                except KeyError:
                    print(f"\"{choice_1}\" IS NOT A VALID INPUT")
        lab_2 = input("\nEnter label for attribute 2: ")
        if lab_2 == "":
            pass
        else:
            while True:
                choice_2 = input("Enter attribute type for choice 2: ")
                try:
                    labels.append(lab_2)
                    att_2 = funcs[choice_2](q=int(quantity), is_called_in_custom=True)
                    break
                except KeyError:
                    print(f"\"{choice_2}\" IS NOT A VALID INPUT")
        lab_3 = input("\nEnter label for attribute 3: ")
        if lab_3 == "":
            pass
        else:
            while True:
                choice_3 = input("Enter attribute type for choice 3: ")
                try:
                    labels.append(lab_3)
                    att_3 = funcs[choice_3](q=int(quantity), is_called_in_custom=True)
                    break
                except KeyError:
                    print(f"\"{choice_3}\" IS NOT A VALID INPUT")
        lab_4 = input("\nEnter label for attribute 4: ")
        if lab_4 == "":
            pass
        else:
            while True:
                choice_4 = input("Enter attribute type for choice 4: ")
                try:
                    labels.append(lab_4)
                    att_4 = funcs[choice_4](q=int(quantity), is_called_in_custom=True)
                    break
                except KeyError:
                    print(f"\"{choice_4}\" IS NOT A VALID INPUT")
        lab_5 = input("\nEnter label for attribute 5: ")
        if lab_5 == "":
            pass
        else:
            while True:
                choice_5 = input("Enter attribute type for choice 5: ")
                try:
                    labels.append(lab_5)
                    att_5 = funcs[choice_5](q=int(quantity), is_called_in_custom=True)
                    break
                except KeyError:
                    print(f"\"{choice_5}\" IS NOT A VALID INPUT")
        lab_6 = input("\nEnter label for attribute 6: ")
        if lab_6 == "":
            pass
        else:
            while True:
                choice_6 = input("Enter attribute type for choice 6: ")
                try:
                    labels.append(lab_6)
                    att_6 = funcs[choice_6](q=int(quantity), is_called_in_custom=True)
                    break
                except KeyError:
                    print(f"\"{choice_6}\" IS NOT A VALID INPUT")
        print(
            f"Here are your choices:\n"
            f"Attribute_1 - Label: {lab_1} | Type: {choice_1}\n"
            f"Attribute_2 - Label: {lab_2} | Type: {choice_2}\n"
            f"Attribute_3 - Label: {lab_3} | Type: {choice_3}\n"
            f"Attribute_4 - Label: {lab_4} | Type: {choice_4}\n"
            f"Attribute_5 - Label: {lab_5} | Type: {choice_5}\n"
            f"Attribute_6 - Label: {lab_6} | Type: {choice_6}\n"
        )
        print("Are these choices correct?")
        confirm = input(f"y/n: ")
        if confirm == "y":
            total.append(labels)
            for s in range(int(quantity)):
                temp = []
                if att_1:
                    if att_1[0] == "name":
                        att_1.remove("name")
                    temp.append(att_1[s])
                else:
                    pass
                if att_2:
                    if att_2[0] == "name":
                        att_2.remove("name")
                    temp.append(att_2[s])
                else:
                    pass
                if att_3:
                    if att_3[0] == "name":
                        att_3.remove("name")
                    temp.append(att_3[s])
                else:
                    pass
                if att_4:
                    if att_4[0] == "name":
                        att_4.remove("name")
                    temp.append(att_4[s])
                else:
                    pass
                if att_5:
                    if att_5[0] == "name":
                        att_5.remove("name")
                    temp.append(att_5[s])
                else:
                    pass
                if att_6:
                    if att_6[0] == "name":
                        att_6.remove("name")
                    temp.append(att_6[s])
                else:
                    pass
                total.append(temp)
            return total
        else:
            pass


def write_file(out_list, write_path=None):
    while True:
        ext = input("Enter desired file_extension. Options are \"txt\" or \"csv\": ")
        file_name = input("Enter file name:  ")
        file_name = re.sub(r'\.\w+', '', file_name)
        if write_path:
            try:
                with open(f"{path}\\{file_name}.{ext}", "w+", newline='') as csvFile:
                    csv_writer = csv.writer(csvFile)
                    for o in out_list:
                        if type(o) is list:
                            csv_writer.writerow(o)
                        else:
                            csv_writer.writerow([o])
                break
            except PermissionError:
                print("CANNOT ACCESS FILE")
                break
            except ValueError:
                print("INVALID INPUT")
                break
            except FileNotFoundError:
                print("FILE PATH NOT FOUND")
                break
            except OSError:
                print("CANNOT SAVE FILE")
                break
        else:
            try:
                with open(f"Output\\{file_name}.{ext}", "w+", newline='') as csvFile:
                    csv_writer = csv.writer(csvFile)
                    for o in out_list:
                        if type(o) is list:
                            csv_writer.writerow(o)
                        else:
                            csv_writer.writerow([o])
                break
            except PermissionError:
                print("CANNOT ACCESS FILE")
                break
            except ValueError:
                print("INVALID INPUT")
                break
            except FileNotFoundError:
                print("FILE PATH NOT FOUND")
                break
            except OSError:
                print("CANNOT SAVE FILE")
                break
    print("\nDONE")


if __name__ == '__main__':
    def settings():
        global path
        while True:
            option = input(
                "\nType \"save path\" to choose a custom path to save generated data to\n"
                "Type \"back\" to go back\n"
                "$: "
            )
            if option == "save path":
                while True:
                    user_path = input(
                        "Enter directory to save data too. To return to the default save folder, type \"default\": ")
                    if os.path.isdir(user_path) is True:
                        with open("SETTINGS DATA - DO NOT DELETE.txt", "w+") as file:
                            file.write(user_path)
                        path = user_path
                        print("SETTINGS SAVED")
                        break
                    elif user_path == "default":
                        path = "default"
                        os.remove("SETTINGS DATA - DO NOT DELETE.txt")
                        break
                    else:
                        print(f"\n\"{user_path}\" NOT A VALID DIRECTORY")
            elif option == "back":
                break
            else:
                print(f"\n\"{option}\" NOT A VALID OPTION\n")


    global path
    if os.path.exists("SETTINGS DATA - DO NOT DELETE.txt") is True:
        with open("SETTINGS DATA - DO NOT DELETE.txt", "r") as settings_file:
            path = settings_file.read()
    else:
        path = "default"
        try:
            os.mkdir("Output")
        except FileExistsError:
            pass
    while True:
        print(f"\nSAVE PATH: {path}")
        print("Random data generator 2.0. Written by: Joshua Kitchen - 2020")
        category = input("For a list of data categories type \"categories\"\nFor settings, type \"settings\"\n"
                         "To exit the program, type \"quit\"\nEnter category: ")
        if category == "categories":
            show_categories()
        elif category == "settings":
            settings()
        elif category == "dates":
            while True:
                back = input("\nIN DATES. To choose another category, type \"back\", otherwise, press \"enter\": ")
                if back == "back":
                    break
                else:
                    output = dates()
                    if path == "default":
                        write_file(output)
                    else:
                        write_file(output, write_path=path)
        elif category == "names":
            while True:
                back = input("\nIN NAMES. To choose another category, type \"back\", otherwise, press \"enter\": ")
                if back == "back":
                    break
                else:
                    output = names()
                    if path == "default":
                        write_file(output)
                    else:
                        write_file(output, write_path=path)
        elif category == "numbers":
            while True:
                back = input("\nIN RANDOM NUMBERS. To choose another category, type \"back\", otherwise, "
                             "press \"enter\": ")
                if back == "back":
                    break
                else:
                    output = numbers()
                    if path == "default":
                        write_file(output)
                    else:
                        write_file(output, write_path=path)
        elif category == "die rolls":
            while True:
                back = input("\nIN DIE ROLLS.. To choose another category, type \"back\", otherwise, press \"enter\": ")
                if back == "back":
                    break
                else:
                    output = die_rolls()
                    if path == "default":
                        write_file(output)
                    else:
                        write_file(output, write_path=path)
        elif category == "coin tosses":
            while True:
                back = input("\nIN COIN TOSSES. To choose another category, type \"back\", otherwise, "
                             "press \"enter\": ")
                if back == "back":
                    break
                else:
                    output = coin_tosses()
                    if path == "default":
                        write_file(output)
                    else:
                        write_file(output, write_path=path)
        elif category == "emails":
            while True:
                back = input("\nIN EMAILS. To choose another category, type \"back\", otherwise, press \"enter\": ")
                if back == "back":
                    break
                else:
                    output = emails()
                    if path == "default":
                        write_file(output)
                    else:
                        write_file(output, write_path=path)
        elif category == "addresses":
            while True:
                back = input("\nIN RANDOM ADDRESSES. To choose another category, type \"back\", otherwise, "
                             "press \"enter\": ")
                if back == "back":
                    break
                else:
                    output = addresses()
                    if path == "default":
                        write_file(output)
                    else:
                        write_file(output, write_path=path)
        elif category == "phone numbers":
            while True:
                back = input("\nIN PHONE NUMBERS. To choose another category, type \"back\", otherwise, press "
                             "\"enter\": ")
                if back == "back":
                    break
                else:
                    output = phone_num()
                    if path == "default":
                        write_file(output)
                    else:
                        write_file(output, write_path=path)
        elif category == "strings and characters":
            while True:
                back = input("\nIN STRINGS AND CHARACTERS. To choose another category, type \"back\", otherwise, press "
                             "\"enter\": ")
                if back == "back":
                    break
                else:
                    output = phone_num()
                    if path == "default":
                        write_file(output)
                    else:
                        write_file(output, write_path=path)
        elif category == "true/false":
            while True:
                back = input("\nTRUE/FALSE. To choose another category, type \"back\", otherwise, press "
                             "\"enter\": ")
                if back == "back":
                    break
                else:
                    output = boolean()
                    if path == "default":
                        write_file(output)
                    else:
                        write_file(output, write_path=path)
        elif category == "random people":
            while True:
                back = input("\nIN RANDOM PEOPLE. To choose another category, type \"back\", otherwise, press "
                             "\"enter\": ")
                if back == "back":
                    break
                else:
                    output = random_people()
                    if path == "default":
                        write_file(output)
                    else:
                        write_file(output, write_path=path)
        elif category == "random students":
            while True:
                back = input("\nIN RANDOM STUDENTS. To choose another category, type \"back\", otherwise, press "
                             "\"enter\": ")
                if back == "back":
                    break
                else:
                    output = random_students()
                    if path == "default":
                        write_file(output)
                    else:
                        write_file(output, write_path=path)
        elif category == "random employees":
            while True:
                back = input("\nIN RANDOM STUDENTS. To choose another category, type \"back\", otherwise, press "
                             "\"enter\": ")
                if back == "back":
                    break
                else:
                    output = random_employees()
                    if path == "default":
                        write_file(output)
                    else:
                        write_file(output, write_path=path)
        elif category == "custom":
            while True:
                back = input("\nIN CUSTOM DATA. To choose another category, type \"back\", otherwise, press "
                             "\"enter\": ")
                if back == "back":
                    output = None
                    break
                else:
                    output = custom_data()
                    break
            while True:
                while True:
                    custom_ext = input("Enter desired file extension. Options are \"txt\" or \"csv\": ")
                    if custom_ext == "csv":
                        break
                    elif custom_ext == "txt":
                        break
                    else:
                        print(f"\"{custom_ext}\" IS NOT A VALID INPUT")
                custom_file_name = input("Enter file name:  ")
                custom_file_name = re.sub(r'\.\w+', '', custom_file_name)
                if path == "default":
                    try:
                        with open(f"Output\\{custom_file_name}.{custom_ext}", "w+", newline='') as custom_file:
                            custom_data_writer = csv.writer(custom_file)
                            for data_set in output:
                                custom_data_writer.writerow(data_set)
                        print("\nDONE")
                        break
                    except PermissionError:
                        print("CANNOT ACCESS FILE")
                        break
                    except ValueError:
                        print("INVALID INPUT")
                        break
                    except FileNotFoundError:
                        print("FILE PATH NOT FOUND")
                        break
                    except OSError:
                        print("CANNOT SAVE FILE")
                        break
                else:
                    try:
                        with open(f"{path}\\{custom_file_name}.{custom_ext}", "w+", newline='') as custom_file:
                            custom_data_writer = csv.writer(custom_file)
                            for data_set in output:
                                custom_data_writer.writerow(data_set)
                        print("\nDONE")
                        break
                    except PermissionError:
                        print("CANNOT ACCESS FILE")
                        break
                    except ValueError:
                        print("INVALID INPUT")
                        break
                    except FileNotFoundError:
                        print("FILE PATH NOT FOUND")
                        break
                    except OSError:
                        print("CANNOT SAVE FILE")
                        break
        elif category == "quit":
            print("Quitting...")
            break
        else:
            print(f"\"{category}\" IS NOT A VALID INPUT")

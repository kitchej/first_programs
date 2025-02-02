"""
WRITTEN BY JOSHUA KITCHEN - Fall and Winter 2019
I wrote this program for practice and personal use. It generates dummy data by using the random module in conjunction
with the databases listed in the import statements, then writes the data to a text file.

 -----------------------------------------------------------------------------------------------------------

CATEGORIES AVAILABLE(version 1.3):
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
- DICE ROLLS (Up to six die)
- COIN TOSSES
- EMAILS
- ADDRESSES
    - Streets (only house numbers and street names)
    - Full (full address with house number, street, city, and state)
- PHONE NUMBERS
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
- CUSTOM DATA **BETA**
    The custom data function allows for the user to create custom data types, similar to RANDOM PEOPLE,
    RANDOM STUDENTS AND RANDOM EMPLOYEES.

    The user will choose attributes for their data objects by selecting different functions that can generate those
    attributes. The max will be 6 attributes per object.

    Attribute types to choose from will include:
    - Names (male, female, mixed, surnames, full male, full female, full mixed)
    - Numbers
    - Characters (Letters of the alphabet or custom data provided by the user)
    - Dates (Full dates, months, and years)
    - Strings (Any custom data provided by the user like city names, company names, book titles, etc.)
    - Boolean statements (True or false statements such as "Is on probation," "Fees paid," "Is in the ICU," etc.)
"""
import random
from datetime import datetime
from Date_data import months, months_to_num
from Names import names_males, names_females, surnames
from Student_data import majors, classes
from Employee_data import positions, salaries
from Address_data import streets, cities, states


def show_categories():
    print("\ndates\nnames\nnumbers\ndice rolls\ncoin tosses\nrandom students\nrandom employees\ncustom")


def random_dates():
    while True:
        command = input("\nIN DATES. To choose another category, type \"back\"\nOptions: full date, months, years\n"
                        "Enter option: ")
        if command == "full date":
            while True:
                path = input("Enter file path to write data to. The only file extension supported in this version is "
                             ".txt: ")
                if ".txt" in path:
                    break
                else:
                    print("\nFILE NAME DOES NOT HAVE A FILE EXTENSION OR INVALID FILE EXTENSION")
            quantity = input("Number of random dates: ")
            form = input("Choose date format \na: month day, year; b:  mm/dd/yyyy; c: day month year d: dd/mm/yyyy: ")
            print("Specify the range of years. For dates in the same year, make the range start and end the same")
            x = input("Range start: ")
            y = input("Range end: ")
            try:
                if form == "a":
                    dates = []
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
                        dates.append(f"{month} {day}, {year}")
                    while True:
                        sort = input("Sort dates in numerical order? y/n: ")
                        if sort == "y":
                            dates.sort(key=lambda date_sort: datetime.strptime(date_sort, '%B %d, %Y'))
                            break
                        elif sort == "n":
                            break
                        else:
                            print(f"\"{sort}\" IS NOT A VALID INPUT")
                    for i in range(int(quantity)):
                        with open(path, "a+") as file:
                            file.write(f"{dates[i]}\n")
                elif form == "b":
                    dates = []
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
                        dates.append(f"{numerical_month}/{day}/{year}")
                    while True:
                        sort = input("Sort dates in numerical order? y/n: ")
                        if sort == "y":
                            dates.sort(key=lambda date_sort: datetime.strptime(date_sort, '%m/%d/%Y'))
                            break
                        elif sort == "n":
                            break
                        else:
                            print(f"\"{sort}\" IS NOT A VALID INPUT")
                    for i in range(int(quantity)):
                        with open(path, "a+") as file:
                            file.write(f"{dates[i]}\n")
                elif form == "c":
                    dates = []
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
                        dates.append(f"{day} {month} {year}")
                    while True:
                        sort = input("Sort dates in numerical order? y/n: ")
                        if sort == "y":
                            dates.sort(key=lambda date_sort: datetime.strptime(date_sort, '%d %B %Y'))
                            break
                        elif sort == "n":
                            break
                        else:
                            print(f"\"{sort}\" IS NOT A VALID INPUT")
                    for i in range(int(quantity)):
                        with open(path, "a+") as file:
                            file.write(f"{dates[i]}\n")
                elif form == "d":
                    dates = []
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
                        dates.append(f"{day}/{numerical_month}/{year}")
                        while True:
                            sort = input("Sort dates in numerical order? y/n: ")
                            if sort == "y":
                                dates.sort(key=lambda date_sort: datetime.strptime(date_sort, '%d/%m/%Y'))
                                break
                            elif sort == "n":
                                break
                            else:
                                print(f"\"{sort}\" IS NOT A VALID INPUT")
                    for i in range(int(quantity)):
                        with open(path, "a+") as file:
                            file.write(f"{dates[i]}\n")
                else:
                    print(f"\"{form}\" IS NOT A VALID INPUT")
                    break
            except PermissionError:
                print("CANNOT ACCESS FILE")
                break
            except FileNotFoundError:
                print("FILE PATH NOT FOUND")
                break
            except OSError:
                print("CANNOT SAVE FILE")
                break
            except ValueError:
                print("INVALID INPUT FOR QUANTITY OR RANGE. Note: \"range start\" must be less than \"range end.\"")
            print("DONE\n")
        elif command == "months":
            while True:
                path = input("Enter file path to write data to. The only file extension supported in this version is "
                             ".txt: ")
                if ".txt" in path:
                    break
                else:
                    print("\nFILE NAME DOES NOT HAVE A FILE EXTENSION OR INVALID FILE EXTENSION")
            quantity = input("Quantity of months: ")
            rand_month = []
            try:
                for i in range(int(quantity)):
                    rand_month.append(random.choice(months))
                for i in range(int(quantity)):
                    with open(path, "a+") as file:
                        file.write(f"{rand_month[i]}\n")
                print("DONE\n")
            except PermissionError:
                print("CANNOT ACCESS FILE")
            except FileNotFoundError:
                print("FILE PATH NOT FOUND")
            except OSError:
                print("CANNOT SAVE FILE")
            except ValueError:
                print("INVALID INPUT FOR QUANTITY")
        elif command == "years":
            while True:
                path = input("Enter file path to write data to. The only file extension supported in this version is "
                             ".txt: ")
                if ".txt" in path:
                    break
                else:
                    print("\nFILE NAME DOES NOT HAVE A FILE EXTENSION OR INVALID FILE EXTENSION")
            quantity = input("Quantity of years: ")
            x = input("Range start: ")
            y = input("Range end: ")
            try:
                rand_year = []
                for i in range(int(quantity)):
                    rand_year.append(random.randint(int(x), int(y)))
                for i in range(int(quantity)):
                    with open(path, "a+") as file:
                        file.write(f"{rand_year[i]}\n")
                print("DONE\n")
            except PermissionError:
                print("CANNOT ACCESS FILE")
            except FileNotFoundError:
                print("FILE PATH NOT FOUND")
            except OSError:
                print("CANNOT SAVE FILE")
            except ValueError:
                print("INVALID INPUT FOR QUANTITY OR RANGE. Note: \"range start\" must be less than \"range end.\"")
        elif command == "back":
            break
        else:
            print(f"\"{command}\" IS NOT A VALID INPUT")


def random_numbers():
    while True:
        command = input("\nIN RANDOM NUMBERS. To go back, type \"back\"\nFor whole numbers only, type \"integers\", "
                        "otherwise press enter to continue: ")
        if command == "integers":
            while True:
                path = input("Enter file path to write data to. The only file extension supported in this version is "
                             ".txt: ")
                if ".txt" in path:
                    break
                else:
                    print("\nFILE NAME DOES NOT HAVE A FILE EXTENSION OR INVALID FILE EXTENSION")
            quantity = input("Quantity of numbers desired: ")
            x = input("Range start: ")
            y = input("Range end: ")
            try:
                for _ in range(int(quantity)):
                    num = random.randint(int(x), int(y))
                    with open(path, "a+") as file:
                        file.write(f"{num}\n")
                print("DONE\n")
            except PermissionError:
                print("CANNOT ACCESS FILE")
            except FileNotFoundError:
                print("FILE PATH NOT FOUND")
            except OSError:
                print("CANNOT SAVE FILE")
            except ValueError:
                print("INVALID INPUT FOR QUANTITY OR RANGE. Note: \"range start\" must be less than \"range end.\"")
        elif command == "":
            while True:
                path = input("Enter file path to write data to. The only file extension supported in this version is "
                             ".txt: ")
                if ".txt" in path:
                    break
                else:
                    print("\nFILE NAME DOES NOT HAVE A FILE EXTENSION OR INVALID FILE EXTENSION")
            quantity = input("Quantity of numbers desired: ")
            x = input("Range start: ")
            y = input("Range end: ")
            r = input("Enter number of decimal places to round to (15 PLACES MAX): ")
            try:
                for _ in range(int(quantity)):
                    num = random.uniform(int(x), int(y))
                    with open(path, "a+") as file:
                        file.write(f"{round(num, int(r))}\n")
                print("DONE\n")
            except PermissionError:
                print("CANNOT ACCESS FILE")
            except FileNotFoundError:
                print("FILE PATH NOT FOUND")
            except OSError:
                print("CANNOT SAVE FILE")
            except ValueError:
                print("INVALID INPUT FOR QUANTITY OR RANGE. Note: \"range start\" must be less than \"range end.\"")
        elif command == "back":
            break
        else:
            print(f"\"{command}\" IS NOT A VALID INPUT")


def random_names():
    while True:
        command = input("\nIN NAMES. To go back, type \"back\"\nCategories: names male, names female, mixed, surnames, "
                        "full names male, full names female, full names mixed\nEnter category: ")
        if command == "names male":
            while True:
                path = input("Enter file path to write data to. The only file extension supported in this version is "
                             ".txt: ")
                if ".txt" in path:
                    break
                else:
                    print("\nFILE NAME DOES NOT HAVE A FILE EXTENSION OR INVALID FILE EXTENSION")
            while True:
                quantity = input("Quantity of names(999 max): ")
                try:
                    if int(quantity) <= 999:
                        break
                    else:
                        print("\nQUANTITY IS TOO LARGE")
                except ValueError:
                    print("\nINVALID INPUT FOR QUANTITY")
            rand_name_males = random.sample(names_males, k=int(quantity))
            try:
                for i in range(int(quantity)):
                    with open(path, "a+") as file:
                        file.write(f"{rand_name_males[i]}\n")
                print("DONE\n")
            except PermissionError:
                print("CANNOT ACCESS FILE")
            except FileNotFoundError:
                print("FILE PATH NOT FOUND")
            except OSError:
                print("CANNOT SAVE FILE")
            except ValueError:
                print("INVALID INPUT FOR QUANTITY")
        elif command == "names female":
            try:
                while True:
                    path = input(
                        "Enter file path to write data to. The only file extension supported in this version is "
                        ".txt: ")
                    if ".txt" in path:
                        break
                    else:
                        print("\nFILE NAME DOES NOT HAVE A FILE EXTENSION OR INVALID FILE EXTENSION")
                while True:
                    quantity = input("Quantity of names: ")
                    try:
                        if int(quantity) <= 999:
                            break
                        else:
                            print("\nQUANTITY IS TOO LARGE")
                    except ValueError:
                        print("\nINVALID INPUT FOR QUANTITY")
                rand_name_females = random.sample(names_females, k=int(quantity))
                for i in range(int(quantity)):
                    with open(path, "a+") as file:
                        file.write(f"{rand_name_females[i]}\n")
                print("DONE\n")
            except PermissionError:
                print("CANNOT ACCESS FILE")
            except FileNotFoundError:
                print("FILE PATH NOT FOUND")
            except OSError:
                print("CANNOT SAVE FILE")
            except ValueError:
                print("INVALID INPUT FOR QUANTITY")
        elif command == "mixed":
            while True:
                path = input("Enter file path to write data to. The only file extension supported in this version is "
                             ".txt: ")
                if ".txt" in path:
                    break
                else:
                    print("\nFILE NAME DOES NOT HAVE A FILE EXTENSION OR INVALID FILE EXTENSION")
            while True:
                quantity = input("Quantity of names: ")
                try:
                    if int(quantity) <= 999:
                        break
                    else:
                        print("\nQUANTITY IS TOO LARGE")
                except ValueError:
                    print("\nINVALID INPUT FOR QUANTITY")
            rand_name_females = random.sample(names_females, k=int(quantity))
            rand_name_males = random.sample(names_males, k=int(quantity))
            try:
                mixed_names = []
                for i in range(int(quantity)):
                    z = random.randint(0, 1)
                    if z == 0:
                        mixed_names.append(rand_name_females[i])
                    else:
                        mixed_names.append(rand_name_males[i])
                for i in range(int(quantity)):
                    with open(path, "a+") as file:
                        file.write(f"{mixed_names[i]}\n")
                print("DONE\n")
            except PermissionError:
                print("CANNOT ACCESS FILE")
            except FileNotFoundError:
                print("FILE PATH NOT FOUND")
            except OSError:
                print("CANNOT SAVE FILE")
            except ValueError:
                print("INVALID INPUT FOR QUANTITY")
        elif command == "surnames":
            while True:
                path = input("Enter file path to write data to. The only file extension supported in this version is "
                             ".txt: ")
                if ".txt" in path:
                    break
                else:
                    print("\nFILE NAME DOES NOT HAVE A FILE EXTENSION OR INVALID FILE EXTENSION")
            while True:
                quantity = input("Quantity of names: ")
                try:
                    if int(quantity) <= 999:
                        break
                    else:
                        print("\nQUANTITY IS TOO LARGE")
                except ValueError:
                    print("\nINVALID INPUT FOR QUANTITY")
            rand_name_surname = random.sample(surnames, k=int(quantity))
            try:
                for i in range(int(quantity)):
                    with open(path, "a+") as file:
                        file.write(f"{rand_name_surname[i]}\n")
                print("DONE\n")
            except PermissionError:
                print("CANNOT ACCESS FILE")
            except FileNotFoundError:
                print("FILE PATH NOT FOUND")
            except OSError:
                print("CANNOT SAVE FILE")
            except ValueError:
                print("INVALID INPUT FOR QUANTITY")
        elif command == "full names male":
            while True:
                path = input("Enter file path to write data to. The only file extension supported in this version is "
                             ".txt: ")
                if ".txt" in path:
                    break
                else:
                    print("\nFILE NAME DOES NOT HAVE A FILE EXTENSION OR INVALID FILE EXTENSION")
            while True:
                quantity = input("Quantity of names: ")
                try:
                    if int(quantity) <= 999:
                        break
                    else:
                        print("\nQUANTITY IS TOO LARGE")
                except ValueError:
                    print("\nINVALID INPUT FOR QUANTITY")
            rand_names_first = random.sample(names_males, k=int(quantity))
            rand_names_last = random.sample(surnames, k=int(quantity))
            try:
                for i in range(int(quantity)):
                    with open(path, "a+") as file:
                        file.write(f"{rand_names_first[i]}  {rand_names_last[i]}\n")
                print("DONE\n")
            except PermissionError:
                print("CANNOT ACCESS FILE")
            except FileNotFoundError:
                print("FILE PATH NOT FOUND")
            except OSError:
                print("CANNOT SAVE FILE")
            except ValueError:
                print("INVALID INPUT FOR QUANTITY")
        elif command == "full names female":
            while True:
                path = input(
                    "Enter file path to write data to. The only file extension supported in this version is "
                    ".txt: ")
                if ".txt" in path:
                    break
                else:
                    print("\nFILE NAME DOES NOT HAVE A FILE EXTENSION OR INVALID FILE EXTENSION")
            while True:
                quantity = input("Quantity of names: ")
                try:
                    if int(quantity) <= 999:
                        break
                    else:
                        print("\nQUANTITY IS TOO LARGE")
                except ValueError:
                    print("\nINVALID INPUT FOR QUANTITY")
            rand_names_first = random.sample(names_females, k=int(quantity))
            rand_names_last = random.sample(surnames, k=int(quantity))
            try:
                for i in range(int(quantity)):
                    with open(path, "a+") as file:
                        file.write(f"{rand_names_first[i]}  {rand_names_last[i]}\n")
                print("DONE\n")
            except PermissionError:
                print("CANNOT ACCESS FILE")
            except ValueError:
                print("INVALID INPUT")
            except FileNotFoundError:
                print("FILE PATH NOT FOUND")
            except OSError:
                print("CANNOT SAVE FILE")
        elif command == "full names mixed":
            while True:
                path = input("Enter file path to write data to. The only file extension supported in this version is "
                             ".txt: ")
                if ".txt" in path:
                    break
                else:
                    print("\nFILE NAME DOES NOT HAVE A FILE EXTENSION OR INVALID FILE EXTENSION")
            while True:
                quantity = input("Quantity of names: ")
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
            try:
                for i in range(int(quantity)):
                    z = random.randint(0, 1)
                    if z == 0:
                        first = rand_names_first_f[i]
                    else:
                        first = rand_names_first_m[i]
                    with open(path, "a+") as file:
                        file.write(f"{first}  {rand_names_last[i]}\n")
                print("DONE\n")
            except PermissionError:
                print("CANNOT ACCESS FILE")
            except FileNotFoundError:
                print("FILE PATH NOT FOUND")
            except OSError:
                print("CANNOT SAVE FILE")
            except ValueError:
                print("INVALID INPUT FOR QUANTITY")
        elif command == "back":
            break
        else:
            print(f"\"{command}\" IS NOT A VALID INPUT")


def dice_rolls():
    while True:
        command = input("\nIN DICE ROLLS. To go back, type \"back\"\nInput number of die (1-6): ")
        if command == "1":
            rolls = input("Quantity of rolls: ")
            while True:
                path = input("Enter file path to write data to. The only file extension supported in this version is "
                             ".txt: ")
                if ".txt" in path:
                    break
                else:
                    print("\nFILE NAME DOES NOT HAVE A FILE EXTENSION OR INVALID FILE EXTENSION")
            try:
                for i in range(int(rolls)):
                    die1 = random.randint(1, 6)
                    with open(path, "a+") as file:
                        file.write(f"{die1}\n")
                print("DONE\n")
            except PermissionError:
                print("CANNOT ACCESS FILE")
            except FileNotFoundError:
                print("FILE PATH NOT FOUND")
            except OSError:
                print("CANNOT SAVE FILE")
            except ValueError:
                print("INVALID INPUT FOR QUANTITY")
        elif command == "2":
            rolls = input("Quantity of rolls: ")
            while True:
                path = input("Enter file path to write data to. The only file extension supported in this version is "
                             ".txt: ")
                if ".txt" in path:
                    break
                else:
                    print("\nFILE NAME DOES NOT HAVE A FILE EXTENSION OR INVALID FILE EXTENSION")
            try:
                for i in range(int(rolls)):
                    die1 = random.randint(1, 6)
                    die2 = random.randint(1, 6)
                    with open(path, "a+") as file:
                        file.write(f"Set {i}: {die1}, {die2}\n")
                print("DONE\n")
            except PermissionError:
                print("CANNOT ACCESS FILE")
            except FileNotFoundError:
                print("FILE PATH NOT FOUND")
            except OSError:
                print("CANNOT SAVE FILE")
            except ValueError:
                print("INVALID INPUT FOR QUANTITY")
        elif command == "3":
            rolls = input("Quantity of rolls: ")
            while True:
                path = input("Enter file path to write data to. The only file extension supported in this version is "
                             ".txt: ")
                if ".txt" in path:
                    break
                else:
                    print("\nFILE NAME DOES NOT HAVE A FILE EXTENSION OR INVALID FILE EXTENSION")
            try:
                for i in range(int(rolls)):
                    die1 = random.randint(1, 6)
                    die2 = random.randint(1, 6)
                    die3 = random.randint(1, 6)
                    with open(path, "a+") as file:
                        file.write(f"Set {i}: {die1}, {die2}, {die3}\n")
                print("DONE\n")
            except PermissionError:
                print("CANNOT ACCESS FILE")
            except FileNotFoundError:
                print("FILE PATH NOT FOUND")
            except OSError:
                print("CANNOT SAVE FILE")
            except ValueError:
                print("INVALID INPUT FOR QUANTITY")
        elif command == "4":
            rolls = input("Quantity of rolls: ")
            while True:
                path = input("Enter file path to write data to. The only file extension supported in this version is "
                             ".txt: ")
                if ".txt" in path:
                    break
                else:
                    print("\nFILE NAME DOES NOT HAVE A FILE EXTENSION OR INVALID FILE EXTENSION")
            try:
                for i in range(int(rolls)):
                    die1 = random.randint(1, 6)
                    die2 = random.randint(1, 6)
                    die3 = random.randint(1, 6)
                    die4 = random.randint(1, 6)
                    with open(path, "a+") as file:
                        file.write(f"Set {i}: {die1}, {die2}, {die3}, {die4}\n")
                print("DONE\n")
            except PermissionError:
                print("CANNOT ACCESS FILE")
            except FileNotFoundError:
                print("FILE PATH NOT FOUND")
            except OSError:
                print("CANNOT SAVE FILE")
            except ValueError:
                print("INVALID INPUT FOR QUANTITY")
        elif command == "5":
            rolls = input("Quantity of rolls: ")
            while True:
                path = input("Enter file path to write data to. The only file extension supported in this version is "
                             ".txt: ")
                if ".txt" in path:
                    break
                else:
                    print("\nFILE NAME DOES NOT HAVE A FILE EXTENSION OR INVALID FILE EXTENSION")
            try:
                for i in range(int(rolls)):
                    die1 = random.randint(1, 6)
                    die2 = random.randint(1, 6)
                    die3 = random.randint(1, 6)
                    die4 = random.randint(1, 6)
                    die5 = random.randint(1, 6)
                    with open(path, "a+") as file:
                        file.write(f"Set {i}: {die1}, {die2}, {die3}, {die4}, {die5}\n")
                print("DONE\n")
            except PermissionError:
                print("CANNOT ACCESS FILE")
            except FileNotFoundError:
                print("FILE PATH NOT FOUND")
            except OSError:
                print("CANNOT SAVE FILE")
            except ValueError:
                print("INVALID INPUT FOR QUANTITY")
        elif command == "6":
            rolls = input("Quantity of rolls: ")
            while True:
                path = input("Enter file path to write data to. The only file extension supported in this version is "
                             ".txt: ")
                if ".txt" in path:
                    break
                else:
                    print("\nFILE NAME DOES NOT HAVE A FILE EXTENSION OR INVALID FILE EXTENSION")
            try:
                for i in range(int(rolls)):
                    die1 = random.randint(1, 6)
                    die2 = random.randint(1, 6)
                    die3 = random.randint(1, 6)
                    die4 = random.randint(1, 6)
                    die5 = random.randint(1, 6)
                    die6 = random.randint(1, 6)
                    with open(path, "a+") as file:
                        file.write(f"Set {i}: {die1}, {die2}, {die3}, {die4}, {die5}, {die6}\n")
                print("DONE\n")
            except PermissionError:
                print("CANNOT ACCESS FILE")
            except FileNotFoundError:
                print("FILE PATH NOT FOUND")
            except OSError:
                print("CANNOT SAVE FILE")
            except ValueError:
                print("INVALID INPUT FOR QUANTITY")
        elif command == "back":
            break
        else:
            print(f"\"{command}\" IS NOT A VALID INPUT")


def coin_tosses():
    while True:
        command = input("\nIN COIN TOSSES. To go back, type \"back\" \nPress ENTER to start")
        if command == "back":
            break
        elif command == "":
            tosses = input("Enter number of tosses: ")
            while True:
                path = input("Enter file path to write data to. The only file extension supported in this version is "
                             ".txt: ")
                if ".txt" in path:
                    break
                else:
                    print("\nFILE NAME DOES NOT HAVE A FILE EXTENSION OR INVALID FILE EXTENSION")
            try:
                for i in range(int(tosses)):
                    toss = random.randint(0, 1)
                    with open(path, "a+") as file:
                        if toss == 0:
                            file.write("Heads\n")
                        else:
                            file.write("Tails\n")
                print("DONE\n")
            except PermissionError:
                print("CANNOT ACCESS FILE")
            except FileNotFoundError:
                print("FILE PATH NOT FOUND")
            except OSError:
                print("CANNOT SAVE FILE")
            except ValueError:
                print("INVALID INPUT FOR QUANTITY")
        else:
            print(f"\"{command}\" IS NOT A VALID INPUT")


def random_students():
    while True:
        student_names = []
        student_gpa = []
        student_majors = []
        student_class = []
        command = input("\nIN RANDOM STUDENT. To choose another category, type \"back\"\nPress enter to start")
        if command == "back":
            break
        elif command == "":
            while True:
                quantity = input("First, enter quantity of students(999 MAX): ")
                try:
                    if int(quantity) <= 999:
                        break
                    else:
                        print("\nQUANTITY IS TOO LARGE")
                except ValueError:
                    print("\nINVALID INPUT FOR QUANTITY")
            name_type = input("Next, enter the type of names for your students\nOptions: a. Male names only, "
                              "b. Female names only c. Mixed: ")
            if name_type == "a":
                rand_names_first_m = random.sample(names_males, k=int(quantity))
                rand_names_last = random.sample(surnames, k=int(quantity))
                for i in range(int(quantity)):
                    student_names.append(f"{rand_names_first_m[i]}  {rand_names_last[i]}")
            elif name_type == "b":
                rand_names_first_f = random.sample(names_females, k=int(quantity))
                rand_names_last = random.sample(surnames, k=int(quantity))
                for i in range(int(quantity)):
                    student_names.append(f"{rand_names_first_f[i]}  {rand_names_last[i]}")
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
            else:
                print(f"\"{name_type}\" IS NOT A VALID INPUT")
            print("Now select some options")
            option_1 = input("Will the student have a GPA? y/n: ")
            try:
                if option_1 == "y":
                    for i in range(int(quantity)):
                        student_gpa.append(round(random.uniform(2.0, 4.0), 2))
                elif option_1 == "n":
                    pass
                else:
                    print(f"\"{option_1}\" IS NOT A VALID INPUT")
                option_2 = input("Will student have a major? y/n: ")
                if option_2 == "y":
                    for i in range(int(quantity)):
                        student_majors.append(random.choice(majors))
                elif option_2 == "n":
                    pass
                else:
                    print(f"\"{option_2}\" IS NOT A VALID INPUT")
                option_3 = input("Will student have a class? y/n: ")
                if option_3 == "y":
                    for i in range(int(quantity)):
                        student_class.append(random.choice(classes))
                elif option_3 == "n":
                    pass
                else:
                    print(f"\"{option_3}\" IS NOT A VALID INPUT")
            except ValueError:
                print("INVALID INPUT")
            while True:
                path = input("Enter file path to write data to. The only file extension supported in this version is "
                             ".txt: ")
                if ".txt" in path:
                    break
                else:
                    print("\nFILE NAME DOES NOT HAVE A FILE EXTENSION OR INVALID FILE EXTENSION")
            for i in range(int(quantity)):
                if student_names:
                    try:
                        with open(path, "a+") as file:
                            file.write(f"{student_names[i]}, ")
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
                    pass
                if student_gpa:
                    try:
                        with open(path, "a+") as file:
                            file.write(f"GPA: {student_gpa[i]}, ")
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
                    pass
                if student_majors:
                    try:
                        with open(path, "a+") as file:
                            file.write(f"Major: {student_majors[i]}, ")
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
                    pass
                if student_class:
                    try:
                        with open(path, "a+") as file:
                            file.write(f"Class: {student_class[i]}, ")
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
                    pass
                try:
                    with open(path, "a+") as file:
                        file.write("\n")
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
            print("DONE\n")
        else:
            print(f"\"{command}\" IS NOT A VALID INPUT")


def random_employees():
    while True:
        employee_names = []
        employee_salary = []
        employee_position = []
        employee_years_worked = []
        command = input("\nIN RANDOM EMPLOYEE. To choose another category, type \"back\"\nPress enter to start")
        if command == "back":
            break
        elif command == "":
            while True:
                quantity = input("First, enter quantity of employees(999 MAX): ")
                try:
                    if int(quantity) <= 999:
                        break
                    else:
                        print("\nQUANTITY IS TOO LARGE")
                except ValueError:
                    print("\nINVALID INPUT FOR QUANTITY")
            name_type = input("Next, enter the type of names for your employees\nOptions: a. Male names only, "
                              "b. Female names only c. Mixed: ")
            if name_type == "a":
                rand_names_first_m = random.sample(names_males, k=int(quantity))
                rand_names_last = random.sample(surnames, k=int(quantity))

                for i in range(int(quantity)):
                    first = rand_names_first_m[i]
                    last = rand_names_last[i]
                    employee_names.append(f"{first} {last}")
            elif name_type == "b":
                rand_names_first_f = random.sample(names_females, k=int(quantity))
                rand_names_last = random.sample(surnames, k=int(quantity))
                for i in range(int(quantity)):
                    first = rand_names_first_f[i]
                    last = rand_names_last[i]
                    employee_names.append(f"{first} {last}")
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
            print("Now select some options")
            option_1 = input("Will the employee have a salary? y/n: ")
            try:
                if option_1 == "y":
                    for i in range(int(quantity)):
                        employee_salary.append(random.choice(salaries))
                elif option_1 == "n":
                    pass
                else:
                    print(f"\"{option_1}\" IS NOT A VALID INPUT")
                option_2 = input("Will employee have a position? y/n: ")
                if option_2 == "y":
                    for i in range(int(quantity)):
                        employee_position.append(random.choice(positions))
                elif option_2 == "n":
                    pass
                else:
                    print(f"\"{option_2}\" IS NOT A VALID INPUT")
                option_3 = input("Will employee have years worked? y/n: ")
                if option_3 == "y":
                    for i in range(int(quantity)):
                        employee_years_worked.append(random.randint(1, 30))
                elif option_3 == "n":
                    pass
                else:
                    print(f"\"{option_3}\" IS NOT A VALID INPUT")
            except ValueError:
                print("INVALID INPUT")
            while True:
                path = input("Enter file path to write data to. The only file extension supported in this version is "
                             ".txt: ")
                if ".txt" in path:
                    break
                else:
                    print("\nFILE NAME DOES NOT HAVE A FILE EXTENSION OR INVALID FILE EXTENSION")
            for i in range(int(quantity)):
                if employee_names:
                    try:
                        with open(path, "a+") as file:
                            file.write(f"{employee_names[i]}, ")
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
                    pass
                if employee_salary:
                    try:
                        with open(path, "a+") as file:
                            file.write(f"Salary: {employee_salary[i]}, ")
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
                    pass
                if employee_position:
                    try:
                        with open(path, "a+") as file:
                            file.write(f"Position: {employee_position[i]}, ")
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
                    pass
                if employee_years_worked:
                    try:
                        with open(path, "a+") as file:
                            file.write(f"Years Worked: {employee_years_worked[i]}, ")
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
                    pass
                try:
                    with open(path, "a+") as file:
                        file.write("\n")
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
            print("DONE\n")
        else:
            print(f"\"{command}\" IS NOT A VALID INPUT")


"""
CUSTOM DATA - WORK IN PROGRESS
----------------------------------------------------------------
The custom data function allows for the user to create custom data types, similar to the built in random_students() and
random_employees() functions.

The user will choose attributes for their data objects by selecting different functions that can generate those
attributes. The max will be 6 attributes per object.

Attribute types to choose from will include:
- Names (male, female, mixed, surnames, full male, full female, full mixed)
- Numbers
- Characters (Letters and other single character symbols)
- Dates (Full dates, timestamps, etc)
- Strings (Cities, words, etc.)
- Boolean statements (True or false statements)
"""


def custom_data():  # *** WORK IN PROGRESS ***

    def name(q):
        while True:
            option = input("\nNAMES\nCategories: names male, names female, mixed, surnames, "
                           "full names male, full names female, full names mixed\nEnter category: ")
            if option == "names male":
                names = random.sample(names_males, int(q))
                print("\nDONE")
                return names
            elif option == "names female":
                names = random.sample(names_females, int(q))
                print("\nDONE")
                return names
            elif option == "surnames":
                names = random.sample(surnames, int(q))
                print("\nDONE")
                return names
            elif option == "mixed":
                while True:
                    m_f = input("Append male or female attribute to name? y/n: ")
                    if m_f == "y":
                        names_m = random.sample(names_males, int(q))
                        names_f = random.sample(names_females, int(q))
                        names = []
                        for i in range(int(q)):
                            n = random.randint(0, 1)
                            if n == 0:
                                names.append(f"{names_m[i]}, M")
                            else:
                                names.append(f"{names_f[i]}, F")
                        print("\nDONE")
                        return names
                    elif m_f == "n":
                        names_m = random.sample(names_males, int(q))
                        names_f = random.sample(names_females, int(q))
                        names = []
                        for i in range(int(q)):
                            n = random.randint(0, 1)
                            if n == 0:
                                names.append(names_m[i])
                            else:
                                names.append(names_f[i])
                        print("\nDONE")
                        return names
                    else:
                        print(f"\"{m_f}\" IS NOT A VALID INPUT")
            elif option == "full names male":
                first = random.sample(names_males, int(q))
                last = random.sample(surnames, int(q))
                names = []
                for i in range(int(q)):
                    names.append(f"{first[i]} {last[i]}")
                print("\nDONE")
                return names
            elif option == "full names female":
                first = random.sample(names_females, int(q))
                last = random.sample(surnames, int(q))
                names = []
                for i in range(int(q)):
                    names.append(f"{first[i]} {last[i]}")
                print("\nDONE")
                return names
            elif option == "full names mixed":
                while True:
                    m_f = input("Append male or female attribute to name? y/n: ")
                    if m_f == "y":
                        first_m = random.sample(names_males, int(q))
                        first_f = random.sample(names_females, int(q))
                        last = random.sample(surnames, int(q))
                        names = []
                        for i in range(int(q)):
                            n = random.randint(0, 1)
                            if n == 0:
                                names.append(f"{first_m[i]} {last[i]}, M")
                            else:
                                names.append(f"{first_f[i]} {last[i]}, F")
                        print("\nDONE")
                        return names
                    elif m_f == "n":
                        first_m = random.sample(names_males, int(q))
                        first_f = random.sample(names_females, int(q))
                        last = random.sample(surnames, int(q))
                        names = []
                        for i in range(int(q)):
                            n = random.randint(0, 1)
                            if n == "0":
                                names.append(f"{first_m[i]} {last[i]}")
                            else:
                                names.append(f"{first_f[i]} {last[i]}")
                        print("\nDONE")
                        return names
                    else:
                        print(f"\"{m_f}\" IS NOT A VALID INPUT")
            else:
                print(f"\"{option}\" IS NOT A VALID INPUT")

    def number(q):
        while True:
            option = input("\nRANDOM NUMBERS\nFor whole numbers only, type \"integers\", "
                           "otherwise press enter to continue: ")
            if option == "integers":
                while True:
                    num_list = []
                    x = input("Range start: ")
                    y = input("Range end: ")
                    try:
                        for _ in range(int(q)):
                            num = random.randint(int(x), int(y))
                            num_list.append(str(num))
                        print("\nDONE")
                        return num_list
                    except ValueError:
                        print("INVALID INPUT FOR QUANTITY OR RANGE. Note: \"range start\" must be less than "
                              "\"range end.\"")
                        break

            elif option == "":
                while True:
                    num_list = []
                    x = input("Range start: ")
                    y = input("Range end: ")
                    r = input("Enter number of decimal places to round to (15 PLACES MAX): ")
                    try:
                        for _ in range(int(q)):
                            num = random.uniform(int(x), int(y))
                            num_list.append(str(round(num, int(r))))
                        print("\nDONE")
                        return num_list
                    except ValueError:
                        print("INVALID INPUT FOR QUANTITY OR RANGE. Note: \"range start\" must be less than "
                              "\"range end.\"")
            else:
                print(f"\"{option}\" IS NOT A VALID INPUT")

    def character(q):
        def str_to_list(raw_data):
            li = list(raw_data.split(", "))
            return li

        alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                    "u", "v", "w", "x", "y", "z"]
        alphabet_capital = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
                            'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        while True:
            print("\nCHARACTER\nOptions: default, default sample, custom\n"
                  "Default will pick a random letter of the alphabet\n"
                  "Default sample will get a sample of the alphabet\n"
                  "Quick custom allows for the addition of a small list of characters"
                  "Custom allows for the use of a user's data bank(see \"custom instructions\" for more information)")
            option = input("\nEnter option: ")
            if option == "default":
                while True:
                    capital = input("Make letters capital?\ny or n: ")
                    if capital == "y":
                        default_choice = random.choices(alphabet_capital, k=int(q))
                        print("\nDONE")
                        return default_choice
                    elif capital == "n":
                        default_choice = random.choices(alphabet, k=int(q))
                        print("\nDONE")
                        return default_choice
                    else:
                        print(f"\"{capital}\" IS NOT A VALID INPUT")
            elif option == "default sample":
                while True:
                    capital = input("Make letters capital?\ny or n: ")
                    if capital == "y":
                        default_sample = random.sample(alphabet_capital, k=int(q))
                        print("\nDONE")
                        return default_sample
                    elif capital == "n":
                        default_sample = random.sample(alphabet, k=int(q))
                        print("\nDONE")
                        return default_sample
                    else:
                        print(f"\"{capital}\" IS NOT A VALID INPUT")
            elif option == "quick custom":
                data = input("Enter desired characters: ")
                user_list = str_to_list(data)
                while True:
                    sample = input("Enter \"choices\" to get a list of randomly selected characters (I.E repeated "
                                   "values possible\nEnter \"sample\" to get a sample of characters (I.E no repeated "
                                   "values) "
                                   "NOTE: If the quantity objects exceeds the size of your list, sample will NOT work ")
                    if sample == "choices":
                        output = random.choices(user_list, k=int(q))
                        print("\nDONE")
                        return output
                    elif sample == "sample":
                        try:
                            output = random.sample(user_list, k=int(q))
                            print("\nDONE")
                            return output
                        except ValueError:
                            print("QUANTITY OF OBJECTS EXCEEDS LIST SIZE")
            elif option == "custom":
                data_name = input("Enter name of data bank: ")
                try:
                    with open(data_name, "r") as file:
                        data_bank = file.read()
                        data_bank = data_bank.strip()
                except PermissionError:
                    print("CANNOT ACCESS FILE")
                except FileNotFoundError:
                    print("FILE PATH NOT FOUND")
                data_list = str_to_list(data_bank)
                while True:
                    print("Enter \"choices\" to get a list of randomly selected characters (I.E repeated values "
                          "possible\nEnter \"sample\" to get a sample of characters (I.E no repeated values)")
                    method = input("Enter option: ")
                    if method == "choices":
                        output = random.choices(data_list, k=int(q))
                        print("\nDONE")
                        return output
                    elif method == "sample":
                        output = random.sample(data_list, k=int(q))
                        print("\nDONE")
                        return output
                    else:
                        print(f"\"{method}\" IS NOT A VALID INPUT")
            else:
                print(f"\"{option}\" IS NOT A VALID INPUT")

    def date(q):
        while True:
            option = input("\nDATE\nOptions: full date, months, years, timestamp(NOT YET AVALIBLE)\n"
                           "Enter option: ")
            if option == "full date":
                while True:
                    form = input("Choose date format \na: month day, year; b:  mm/dd/yyyy; c: day month year "
                                 "d: dd/mm/yyyy: ")
                    if form == "a":
                        while True:
                            print(
                                "Specify the range of years. For dates in the same year, make the range start and end "
                                "the same")
                            x = input("Range start: ")
                            y = input("Range end: ")
                            if int(x) <= int(y):
                                break
                            else:
                                print("\n\"Range start\" MUST BE SMALLER THAN \"Range end\"")
                        dates = []
                        for i in range(int(q)):
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
                            dates.append(f"{month} {str(day)}, {str(year)}")
                        sort_option = input("Sort dates? Options: sort ascending, sort descending, no sort: ")
                        while True:
                            if sort_option == "sort ascending":
                                dates.sort(key=lambda date_sort: datetime.strptime(date_sort, '%B %d, %Y'))
                                print("\nDONE")
                                return dates
                            elif sort_option == "sort descending":
                                dates.sort(reverse=True, key=lambda date_sort: datetime.strptime(date_sort,
                                           '%B %d, %Y'))
                                print("\nDONE")
                                return dates
                            elif sort_option == "no sort":
                                print("\nDONE")
                                return dates
                            else:
                                print(f"\"{sort_option}\" IS NOT A VALID INPUT")
                    elif form == "b":
                        while True:
                            print(
                                "Specify the range of years. For dates in the same year, make the range start and end "
                                "the same")
                            x = input("Range start: ")
                            y = input("Range end: ")
                            if int(x) <= int(y):
                                break
                            else:
                                print("\n\"Range start\" MUST BE SMALLER THAN \"Range end\"")
                        dates = []
                        for i in range(int(q)):
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
                            dates.append(f"{str(numerical_month)}/{str(day)}/{str(year)}")
                        sort_option = input("Sort dates? Options: sort ascending, sort descending, no sort: ")
                        while True:
                            if sort_option == "sort ascending":
                                dates.sort(key=lambda date_sort: datetime.strptime(date_sort, '%m/%d/%Y'))
                                print("\nDONE")
                                return dates
                            elif sort_option == "sort descending":
                                dates.sort(reverse=True, key=lambda date_sort: datetime.strptime(date_sort, '%m/%d/%Y'))
                                print("\nDONE")
                                return dates
                            elif sort_option == "no sort":
                                print("\nDONE")
                                return dates
                            else:
                                print(f"\"{sort_option}\" IS NOT A VALID INPUT")
                    elif form == "c":
                        print("Specify the range of years. For dates in the same year, make the range start and end "
                              "the same")
                        while True:
                            x = input("Range start: ")
                            y = input("Range end: ")
                            if int(x) <= int(y):
                                break
                            else:
                                print("\n\"Range start\" MUST BE SMALLER THAN \"Range end\"")
                        dates = []
                        for i in range(int(q)):
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
                            dates.append(f"{str(day)} {month} {str(year)}")
                        sort_option = input("Sort dates? Options: sort ascending, sort descending, no sort: ")
                        while True:
                            if sort_option == "sort ascending":
                                dates.sort(key=lambda date_sort: datetime.strptime(date_sort, '%d %B %Y'))
                                print("\nDONE")
                                return dates
                            elif sort_option == "sort descending":
                                dates.sort(reverse=True, key=lambda date_sort: datetime.strptime(date_sort, '%d %B %Y'))
                                print("\nDONE")
                                return dates
                            elif sort_option == "no sort":
                                print("\nDONE")
                                return dates
                            else:
                                print(f"\"{sort_option}\" IS NOT A VALID INPUT")
                    elif form == "d":
                        print("Specify the range of years. For dates in the same year, make the range start and end "
                              "the same")
                        while True:
                            x = input("Range start: ")
                            y = input("Range end: ")
                            if int(x) <= int(y):
                                break
                            else:
                                print("\n\"Range start\" MUST BE SMALLER THAN \"Range end\"")
                        dates = []
                        for i in range(int(q)):
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
                            dates.append(f"{str(day)}/{str(numerical_month)}/{str(year)}")
                        sort_option = input("Sort dates? Options: sort ascending, sort descending, no sort: ")
                        while True:
                            if sort_option == "sort ascending":
                                dates.sort(key=lambda date_sort: datetime.strptime(date_sort, '%d/%m/%Y'))
                                print("\nDONE")
                                return dates
                            elif sort_option == "sort descending":
                                dates.sort(reverse=True, key=lambda date_sort: datetime.strptime(date_sort, '%d/%m/%Y'))
                                print("\nDONE")
                                return dates
                            elif sort_option == "no sort":
                                print("\nDONE")
                                return dates
                            else:
                                print(f"\"{sort_option}\" IS NOT A VALID INPUT")
                    else:
                        print(f"\"{form}\" IS NOT A VALID INPUT")
                        break
            elif option == "months":
                rand_month = []
                for i in range(int(q)):
                    rand_month.append(random.choice(months))
                while True:
                    sort_option = input("Sort dates? Options: sort ascending, sort descending, no sort: ")
                    if sort_option == "sort ascending: ":
                        rand_month.sort(key=lambda date_sort: datetime.strptime(date_sort, '%B'))
                        print("\nDONE")
                        return rand_month
                    elif sort_option == "sort descending":
                        rand_month.sort(reverse=True, key=lambda date_sort: datetime.strptime(date_sort, '%B'))
                        print("\nDONE")
                        return rand_month
                    elif sort_option == "no sort":
                        print("\nDONE")
                        return rand_month
                    else:
                        print(f"\"{sort_option}\" IS NOT A VALID INPUT")
            elif option == "years":
                while True:
                    print("Specify the range of years")
                    x = input("Range start: ")
                    y = input("Range end: ")
                    if int(x) <= int(y):
                        break
                    else:
                        print("\n\"Range start\" MUST BE SMALLER THAN \"Range end\"")
                rand_year = []
                for i in range(int(q)):
                    rand_year.append(random.randint(int(x), int(y)))
                while True:
                    sort_option = input("Sort dates? Options: sort ascending, sort descending, no sort: ")
                    if sort_option == "sort ascending: ":
                        print("\nDONE")
                        return rand_year
                    elif sort_option == "sort descending":
                        rand_year.sort(reverse=True)
                        print("\nDONE")
                        return rand_year
                    elif sort_option == "no sort":
                        print("\nDONE")
                        return rand_year
                    else:
                        print(f"\"{sort_option}\" IS NOT A VALID INPUT")
            elif option == "timestamp":  # Work in progress
                print("FEATURE NOT YET AVAILABLE")

            else:
                print(f"\"{option}\" IS NOT A VALID INPUT")

    def string(q):

        def str_to_list(raw_data):
            li = list(raw_data.split(", "))
            return li

        print("\nSTRING")
        data_name = input("Enter file path to data bank: ")
        with open(data_name, "r") as file:
            data_bank = file.read()
        data = str_to_list(data_bank)
        while True:
            sample = input("Type \"choices\" to randomly choose data (Duplicated values possible). Type \"sample\" to "
                           "get a sample of data (No duplicate values): ")
            if sample == "choices":
                output = random.choices(data, k=int(q))
                break
            elif sample == "sample":
                output = random.sample(data, k=int(q))
                break
            else:
                print(f"\"{sample}\" IS NOT A VALID INPUT")
        while True:
            sort_option = input("Sort data in alphabetical order? Options: sort ascending, sort descending, no sort: ")
            if sort_option == "sort ascending":
                output.sort()
                print("\nDONE")
                return output
            elif sort_option == "sort descending":
                output.sort(reverse=True)
                print("\nDONE")
                return output
            elif sort_option == "no sort":
                print("\nDONE")
                return output
            else:
                print(f"\"{sort_option}\" IS NOT A VALID INPUT")

    def boolean(q):
        print("\nBOOLEAN\nEnter a boolean statement\nExample: \"Is on probation\", \"Is in the ICU\", \"Fees paid\"")
        statement = input("Statement: ")
        output = []
        for i in range(int(q)):
            n = random.randint(0, 1)
            if n == 0:
                output.append(f"{statement}: True")
            else:
                output.append(f"{statement}: False")
        print("\nDONE")
        return output

    while True:
        command = input("\nIN CUSTOM DATA. To go back, type \"back\" For help, type \"help\"\nOtherwise press \"enter\""
                        "to start: ")
        if command == "back":
            break
        elif command == "help":
            with open("custom_instructions.txt", "r") as file:
                print(file.read())
        elif command == "":
            while True:
                path = input("Enter file path to write data to. The only file extension supported in this version is "
                             ".txt: ")
                if ".txt" in path:
                    break
                else:
                    print("\nFILE NAME DOES NOT HAVE A FILE EXTENSION OR INVALID FILE EXTENSION")
            while True:
                quantity = input("Quantity of objects (MAX 999): ")
                try:
                    if int(quantity) <= 999:
                        break
                    else:
                        print("\nQUANTITY IS TOO LARGE")
                except ValueError:
                    print("\nINVALID INPUT FOR QUANTITY")
            print("Next, choose what type of data each attribute  will be. The max is six. If an attribute will not be "
                  "used, type \"pass\"")
            att_1 = []
            att_2 = []
            att_3 = []
            att_4 = []
            att_5 = []
            att_6 = []
            label_1 = None
            label_2 = None
            label_3 = None
            label_4 = None
            label_5 = None
            label_6 = None

            while True:
                choice1 = input("Enter attribute 1 type: ")
                if choice1 == "pass":
                    break
                elif choice1 == "name":
                    label_1 = input("Enter label for attribute: ")
                    att_1 = name(quantity)
                    break
                elif choice1 == "number":
                    label_1 = input("Enter label for attribute: ")
                    att_1 = number(quantity)
                    break
                elif choice1 == "character":
                    label_1 = input("Enter label for attribute: ")
                    att_1 = character(quantity)
                    break
                elif choice1 == "date":
                    label_1 = input("Enter label for attribute: ")
                    att_1 = date(quantity)
                    break
                elif choice1 == "string":
                    label_1 = input("Enter label for attribute: ")
                    att_1 = string(quantity)
                    break
                elif choice1 == "boolean":
                    label_1 = input("Enter label for attribute: ")
                    att_1 = boolean(quantity)
                    break
                else:
                    print(f"\"{choice1}\" IS NOT A VALID INPUT")
            while True:
                choice2 = input("Enter attribute 2 type: ")
                if choice2 == "pass":
                    break
                elif choice2 == "name":
                    label_2 = input("Enter label for attribute: ")
                    att_2 = name(quantity)
                    break
                elif choice2 == "number":
                    label_2 = input("Enter label for attribute: ")
                    att_2 = number(quantity)
                    break
                elif choice2 == "character":
                    label_2 = input("Enter label for attribute: ")
                    att_2 = character(quantity)
                    break
                elif choice2 == "date":
                    label_2 = input("Enter label for attribute: ")
                    att_2 = date(quantity)
                    break
                elif choice2 == "string":
                    label_2 = input("Enter label for attribute: ")
                    att_2 = string(quantity)
                    break
                elif choice2 == "boolean":
                    label_2 = input("Enter label for attribute: ")
                    att_2 = boolean(quantity)
                    break
                else:
                    print(f"\"{choice2}\" IS NOT A VALID INPUT")
            while True:
                choice3 = input("Enter attribute 3 type: ")
                if choice3 == "pass":
                    break
                elif choice3 == "name":
                    label_3 = input("Enter label for attribute: ")
                    att_3 = name(quantity)
                    break
                elif choice3 == "number":
                    label_3 = input("Enter label for attribute: ")
                    att_3 = number(quantity)
                    break
                elif choice3 == "character":
                    label_3 = input("Enter label for attribute: ")
                    att_3 = character(quantity)
                    break
                elif choice3 == "date":
                    label_3 = input("Enter label for attribute: ")
                    att_3 = date(quantity)
                    break
                elif choice3 == "string":
                    label_3 = input("Enter label for attribute: ")
                    att_3 = string(quantity)
                    break
                elif choice3 == "boolean":
                    label_3 = input("Enter label for attribute: ")
                    att_3 = boolean(quantity)
                    break
                else:
                    print(f"\"{choice3}\" IS NOT A VALID INPUT")
            while True:
                choice4 = input("Enter attribute 4 type: ")
                if choice4 == "pass":
                    break
                elif choice4 == "name":
                    label_4 = input("Enter label for attribute")
                    att_4 = name(quantity)
                    break
                elif choice4 == "number":
                    label_4 = input("Enter label for attribute")
                    att_4 = number(quantity)
                    break
                elif choice4 == "character":
                    label_4 = input("Enter label for attribute")
                    att_4 = character(quantity)
                    break
                elif choice4 == "date":
                    label_4 = input("Enter label for attribute")
                    att_4 = date(quantity)
                    break
                elif choice4 == "string":
                    label_4 = input("Enter label for attribute")
                    att_4 = string(quantity)
                    break
                elif choice4 == "boolean":
                    label_4 = input("Enter label for attribute")
                    att_4 = boolean(quantity)
                    break
                else:
                    print(f"\"{choice4}\" IS NOT A VALID INPUT")
            while True:
                choice5 = input("Enter attribute 5 type: ")
                if choice5 == "pass":
                    break
                elif choice5 == "name":
                    label_5 = input("Enter label for attribute")
                    att_5 = name(quantity)
                    break
                elif choice5 == "number":
                    label_5 = input("Enter label for attribute")
                    att_5 = number(quantity)
                    break
                elif choice5 == "character":
                    label_5 = input("Enter label for attribute")
                    att_5 = character(quantity)
                    break
                elif choice5 == "date":
                    label_5 = input("Enter label for attribute")
                    att_5 = date(quantity)
                    break
                elif choice5 == "string":
                    label_5 = input("Enter label for attribute")
                    att_5 = string(quantity)
                    break
                elif choice5 == "boolean":
                    label_5 = input("Enter label for attribute")
                    att_5 = boolean(quantity)
                    break
                else:
                    print(f"\"{choice5}\" IS NOT A VALID INPUT")
            while True:
                choice6 = input("Enter attribute 6 type: ")
                if choice6 == "pass":
                    break
                elif choice6 == "name":
                    label_6 = input("Enter label for attribute")
                    att_6 = name(quantity)
                    break
                elif choice6 == "number":
                    label_6 = input("Enter label for attribute")
                    att_6 = number(quantity)
                    break
                elif choice6 == "character":
                    label_6 = input("Enter label for attribute")
                    att_6 = character(quantity)
                    break
                elif choice6 == "date":
                    label_6 = input("Enter label for attribute")
                    att_6 = date(quantity)
                    break
                elif choice6 == "string":
                    label_6 = input("Enter label for attribute")
                    att_6 = string(quantity)
                    break
                elif choice6 == "boolean":
                    label_6 = input("Enter label for attribute")
                    att_6 = boolean(quantity)
                    break
                else:
                    print(f"\"{choice6}\" IS NOT A VALID INPUT")
            try:
                with open(path, "a+") as file:
                    if att_1:
                        file.write(f"{label_1}, ")
                    else:
                        pass
                    if att_2:
                        file.write(f"{label_2}, ")
                    else:
                        pass
                    if att_3:
                        file.write(f"{label_3}, ")
                    else:
                        pass
                    if att_4:
                        file.write(f"{label_4}, ")
                    else:
                        pass
                    if att_5:
                        file.write(f"{label_5}, ")
                    else:
                        pass
                    if att_6:
                        file.write(f"{label_6}, ")
                    else:
                        pass
                    file.write("\n")
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
            for i in range(int(quantity)):
                try:
                    with open(path, "a+") as file:
                        if att_1:
                            file.write(f"{att_1[i]}, ")
                        else:
                            pass
                        if att_2:
                            file.write(f"{att_2[i]}, ")
                        else:
                            pass
                        if att_3:
                            file.write(f"{att_3[i]}, ")
                        else:
                            pass
                        if att_4:
                            file.write(f"{att_4[i]}, ")
                        else:
                            pass
                        if att_5:
                            file.write(f"{att_5[i]}, ")
                        else:
                            pass
                        if att_6:
                            file.write(f"{att_6[i]}, ")
                        else:
                            pass
                        file.write("\n")
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

        else:
            print(f"\"{command}\" IS NOT A VALID INPUT")


def emails():
    while True:
        command = input("\nIN EMAILS. To go back, type \"back\". Press \"enter\" to continue: ")
        if command == "back":
            break
        else:
            while True:
                path = input("Enter file path to write data to. The only file extension supported in this version is "
                             ".txt: ")
                if ".txt" in path:
                    break
                else:
                    print("\nFILE NAME DOES NOT HAVE A FILE EXTENSION OR INVALID FILE EXTENSION")
            while True:
                quantity = input("Quantity of emails(999 max): ")
                try:
                    if int(quantity) <= 999:
                        break
                    else:
                        print("\nQUANTITY IS TOO LARGE")
                except ValueError:
                    print("\nINVALID INPUT FOR QUANTITY")
            domains = ["gmail.com", "yahoo.com", "hotmail.com", "aol.com"]
            try:
                with open(path, "a+") as file:
                    for i in range(int(quantity)):
                        var = random.randint(0, 2)
                        if var == 0:
                            first = random.choice(names_males)
                            last = random.choice(surnames)
                            var_1 = random.randint(0, 1)
                            if var_1 == 0:
                                file.write(f"{first.lower()}.{last.lower()}@{random.choice(domains)}\n")
                            else:
                                file.write(f"{last.lower()}.{first.lower()}@{random.choice(domains)}\n")
                        elif var == 2:
                            name_var = random.randint(0, 1)
                            if name_var == 0:
                                first = random.choice(names_males)
                            else:
                                first = random.choice(names_females)
                            last = random.choice(surnames)
                            file.write(f"{first.lower()}{last[0]}{random.randint(100, 9999)}"
                                       f"@{random.choice(domains)}\n")
                        else:
                            name_var = random.randint(0, 1)
                            if name_var == 0:
                                first = random.choice(names_males)
                            else:
                                first = random.choice(names_females)
                            last = random.choice(surnames)
                            var_2 = random.randint(0, 1)
                            if var_2 == 0:
                                file.write(f"{first.lower()}.{random.randint(100, 9999)}@{random.choice(domains)}\n")
                            else:
                                file.write(f"{random.randint(100, 9999)}.{first.lower()}@{random.choice(domains)}\n")
            except PermissionError:
                print("CANNOT ACCESS FILE")
            except FileNotFoundError:
                print("FILE PATH NOT FOUND")
            except OSError:
                print("CANNOT SAVE FILE")
            except ValueError:
                print("INVALID INPUT FOR QUANTITY")
        print("DONE\n")


def random_addresses():
    while True:
        command = input("\nIN ADDRESSES. To go back, type \"back\" \nOptions - \"street\"(just the house number and "
                        "street) or \"full\"(full address with house number, street, city, and state): ")
        if command == "back":
            break
        else:
            while True:
                path = input("Enter file path to write data to. The only file extension supported in this version is "
                             ".txt: ")
                if ".txt" in path:
                    break
                else:
                    print("\nFILE NAME DOES NOT HAVE A FILE EXTENSION OR INVALID FILE EXTENSION")
            while True:
                quantity = input("Quantity of addresses(999 max): ")
                try:
                    if int(quantity) <= 999:
                        break
                    else:
                        print("\nQUANTITY IS TOO LARGE")
                except ValueError:
                    print("\nINVALID INPUT FOR QUANTITY")
            if command == "street":
                with open(path, "a+") as file:
                    s = random.sample(streets, k=int(quantity))
                    try:
                        for i in range(int(quantity)):
                            house_num = random.randint(1, 9999)
                            street = s[i]
                            file.write(f"{house_num} {street}\n")
                    except PermissionError:
                        print("CANNOT ACCESS FILE")
                    except FileNotFoundError:
                        print("FILE PATH NOT FOUND")
                    except OSError:
                        print("CANNOT SAVE FILE")
                    except ValueError:
                        print("INVALID INPUT FOR QUANTITY")
                print("DONE\n")
            elif command == "full":
                with open(path, "a+") as file:
                    s = random.sample(streets, k=int(quantity))
                    c = random.sample(cities, k=int(quantity))
                    sa = random.choices(states, k=int(quantity))
                    try:
                        for i in range(int(quantity)):
                            house_num = random.randint(1, 9999)
                            street = s[i]
                            city = c[i]
                            state = sa[i]
                            file.write(f"{house_num} {street}, {city}, {state}\n")
                    except PermissionError:
                        print("CANNOT ACCESS FILE")
                    except FileNotFoundError:
                        print("FILE PATH NOT FOUND")
                    except OSError:
                        print("CANNOT SAVE FILE")
                    except ValueError:
                        print("INVALID INPUT FOR QUANTITY")
                print("DONE\n")
            else:
                print(f"\"{command}\" is not a valid input")


def random_phone_num():
    area_codes = [201, 202, 203, 205, 206, 207, 208, 209, 210, 212, 213, 214, 215, 216, 217, 218, 219, 220, 224, 225,
                  228, 229, 231, 234, 239, 240, 248, 251, 252, 253, 254, 256, 260, 262, 267, 269, 270, 272, 276, 281,
                  301, 302, 303, 304, 305, 307, 308, 309, 310, 312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 323,
                  325, 330, 331, 334, 336, 337, 339, 346, 347, 351, 352, 360, 361, 364, 385, 386, 401, 402, 404, 405,
                  406, 407, 408, 409, 410, 412, 413, 414, 415, 417, 419, 423, 424, 425, 432, 434, 435, 440, 442, 443,
                  458, 469, 478, 479, 480, 484, 501, 502, 503, 504, 505, 507, 508, 509, 510, 512, 513, 515, 516, 517,
                  518, 520, 530, 531, 539, 540, 541, 551, 559, 561, 562, 563, 567, 570, 571, 573, 574, 575, 580, 585,
                  586, 601, 602, 603, 605, 606, 607, 608, 609, 610, 612, 614, 615, 616, 617, 618, 619, 620, 623, 626,
                  628, 629, 630, 631, 636, 641, 646, 650, 651, 657, 660, 661, 662, 667, 669, 678, 681, 682, 701, 702,
                  703, 704, 706, 707, 708, 712, 713, 714, 715, 716, 717, 718, 719, 720, 724, 725, 727, 731, 732, 734,
                  737, 740, 743, 747, 754, 757, 760, 762, 763, 765, 769, 770, 772, 773, 774, 775, 779, 781, 785, 786,
                  801, 802, 803, 804, 805, 806, 808, 810, 812, 813, 814, 815, 816, 817, 818, 828, 830, 831, 832, 843,
                  845, 847, 848, 850, 856, 857, 858, 859, 860, 862, 863, 864, 865, 870, 878, 901, 903, 904, 907, 908,
                  909, 910, 912, 913, 914, 915, 916, 917, 918, 919, 920, 925, 928, 929, 930, 931, 936, 937, 940, 941,
                  947, 949, 951, 952, 954, 956, 959, 970, 971, 972, 973, 978, 979, 980, 984, 985, 989, 854]

    while True:
        command = input("\nIN PHONE NUMBERS. To go back, type \"back\". Press \"enter\" to continue: ")
        if command == "back":
            break
        else:
            while True:
                path = input("Enter file path to write data to. The only file extension supported in this version is "
                             ".txt: ")
                if ".txt" in path:
                    break
                else:
                    print("\nFILE NAME DOES NOT HAVE A FILE EXTENSION OR INVALID FILE EXTENSION")
            while True:
                quantity = input("Quantity of addresses(999 max): ")
                try:
                    if int(quantity) <= 999:
                        break
                    else:
                        print("\nQUANTITY IS TOO LARGE")
                except ValueError:
                    print("\nINVALID INPUT FOR QUANTITY")

            try:
                with open(path, "a+") as file:
                    for i in range(int(quantity)):
                        file.write(f"{random.choice(area_codes)}-{random.randint(100, 999)}"
                                   f"-{random.randint(1000, 9999)}\n")
            except PermissionError:
                print("CANNOT ACCESS FILE")
            except FileNotFoundError:
                print("FILE PATH NOT FOUND")
            except OSError:
                print("CANNOT SAVE FILE")
            except ValueError:
                print("INVALID INPUT FOR QUANTITY")
            print("DONE\n")


def random_people():
    while True:
        people_names = []
        people_addresses = []
        people_emails = []
        people_numbers = []
        command = input("\nIN RANDOM PEOPLE. To choose another category, type \"back\"\nPress enter to start ")
        if command == "back":
            break
        else:
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
                path = input("Enter file path to write data to. The only file extension supported in this version is "
                             ".txt: ")
                if ".txt" in path:
                    break
                else:
                    print("\nFILE NAME DOES NOT HAVE A FILE EXTENSION OR INVALID FILE EXTENSION")
            name_type = input("Next, enter the type of names you want\nOptions: a. Male names only, "
                              "b. Female names only c. Mixed: ")
            if name_type == "a":
                rand_names_first_m = random.sample(names_males, k=int(quantity))
                rand_names_last = random.sample(surnames, k=int(quantity))
                for i in range(int(quantity)):
                    people_names.append(f"{rand_names_first_m[i]}  {rand_names_last[i]}")
            elif name_type == "b":
                rand_names_first_f = random.sample(names_females, k=int(quantity))
                rand_names_last = random.sample(surnames, k=int(quantity))
                for i in range(int(quantity)):
                    people_names.append(f"{rand_names_first_f[i]}  {rand_names_last[i]}")
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
            else:
                print(f"\"{name_type}\" IS NOT A VALID INPUT")
            print("Now select some options")
            option_1 = input("Will the people have an address? y/n: ")
            try:
                if option_1 == "y":
                    street = random.sample(streets, k=int(quantity))
                    city = random.sample(cities, k=int(quantity))
                    for i in range(int(quantity)):
                        people_addresses.append(f"{random.randint(1, 9999)} {street[i]}, {city[i]}, "
                                                f"{random.choice(states)}")
                elif option_1 == "n":
                    pass
                else:
                    print(f"\"{option_1}\" IS NOT A VALID INPUT")
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
                                var_2 = random.randint(0,1)
                                if var_2 == 0:
                                    people_emails.append(
                                        f"{s[0].lower()}{s[1][0]}{random.randint(100, 9999)}@{random.choice(domains)}")
                                else:
                                    people_emails.append(
                                        f"{s[1][0]}{s[0].lower()}{random.randint(100, 9999)}@{random.choice(domains)}")
                            except IndexError:
                                people_emails.append(f"{s[0].lower()}{random.randint(100, 9999)}"
                                                     f"@{random.choice(domains)}")
                        else:
                            people_emails.append(f"{s[0].lower()}{random.randint(100, 9999)}@{random.choice(domains)}")

                elif option_2 == "n":
                    pass
                else:
                    print(f"\"{option_2}\" IS NOT A VALID INPUT")
                option_3 = input("Will people have a phone number? y/n: ")
                if option_3 == "y":
                    area_codes = [201, 202, 203, 205, 206, 207, 208, 209, 210, 212, 213, 214, 215, 216, 217, 218, 219,
                                  220, 224, 225,
                                  228, 229, 231, 234, 239, 240, 248, 251, 252, 253, 254, 256, 260, 262, 267, 269, 270,
                                  272, 276, 281,
                                  301, 302, 303, 304, 305, 307, 308, 309, 310, 312, 313, 314, 315, 316, 317, 318, 319,
                                  320, 321, 323,
                                  325, 330, 331, 334, 336, 337, 339, 346, 347, 351, 352, 360, 361, 364, 385, 386, 401,
                                  402, 404, 405,
                                  406, 407, 408, 409, 410, 412, 413, 414, 415, 417, 419, 423, 424, 425, 432, 434, 435,
                                  440, 442, 443,
                                  458, 469, 478, 479, 480, 484, 501, 502, 503, 504, 505, 507, 508, 509, 510, 512, 513,
                                  515, 516, 517,
                                  518, 520, 530, 531, 539, 540, 541, 551, 559, 561, 562, 563, 567, 570, 571, 573, 574,
                                  575, 580, 585,
                                  586, 601, 602, 603, 605, 606, 607, 608, 609, 610, 612, 614, 615, 616, 617, 618, 619,
                                  620, 623, 626,
                                  628, 629, 630, 631, 636, 641, 646, 650, 651, 657, 660, 661, 662, 667, 669, 678, 681,
                                  682, 701, 702,
                                  703, 704, 706, 707, 708, 712, 713, 714, 715, 716, 717, 718, 719, 720, 724, 725, 727,
                                  731, 732, 734,
                                  737, 740, 743, 747, 754, 757, 760, 762, 763, 765, 769, 770, 772, 773, 774, 775, 779,
                                  781, 785, 786,
                                  801, 802, 803, 804, 805, 806, 808, 810, 812, 813, 814, 815, 816, 817, 818, 828, 830,
                                  831, 832, 843,
                                  845, 847, 848, 850, 856, 857, 858, 859, 860, 862, 863, 864, 865, 870, 878, 901, 903,
                                  904, 907, 908,
                                  909, 910, 912, 913, 914, 915, 916, 917, 918, 919, 920, 925, 928, 929, 930, 931, 936,
                                  937, 940, 941,
                                  947, 949, 951, 952, 954, 956, 959, 970, 971, 972, 973, 978, 979, 980, 984, 985, 989,
                                  854]
                    for i in range(int(quantity)):
                        people_numbers.append(f"{random.choice(area_codes)}-{random.randint(100, 999)}"
                                              f"-{random.randint(1000, 9999)}")
                elif option_3 == "n":
                    pass
                else:
                    print(f"\"{option_3}\" IS NOT A VALID INPUT")
            except ValueError:
                print("INVALID INPUT")
            for i in range(int(quantity)):
                if people_names:
                    try:
                        with open(path, "a+") as file:
                            file.write(f"{people_names[i]}; ")
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
                    pass
                if people_addresses:
                    try:
                        with open(path, "a+") as file:
                            file.write(f"{people_addresses[i]}; ")
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
                    pass
                if people_emails:
                    try:
                        with open(path, "a+") as file:
                            file.write(f"{people_emails[i]}; ")
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
                    pass
                if people_numbers:
                    try:
                        with open(path, "a+") as file:
                            file.write(f"{people_numbers[i]}; ")
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
                    pass
                try:
                    with open(path, "a+") as file:
                        file.write("\n")
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
            print("DONE\n")


while True:
    print("\nRandom data generator. Written by: Joshua Kitchen - 2019")
    category = input("For a list of data categories type \"categories\"\nTo exit the program, type \"quit\""
                     "\nEnter category: ")
    if category == "categories":
        show_categories()
    elif category == "dates":
        random_dates()
    elif category == "names":
        random_names()
    elif category == "numbers":
        random_numbers()
    elif category == "dice rolls":
        dice_rolls()
    elif category == "coin tosses":
        coin_tosses()
    elif category == "random students":
        random_students()
    elif category == "random employees":
        random_employees()
    elif category == "custom":
        custom_data()
    elif category == "emails":
        emails()
    elif category == "addresses":
        random_addresses()
    elif category == "phone numbers":
        random_phone_num()
    elif category == "random people":
        random_people()
    elif category == "quit":
        print("Quitting...")
        break
    else:
        print(f"\"{category}\" IS NOT A VALID INPUT")

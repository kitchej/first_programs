from tkinter import *
from tkinter import filedialog
import tkinter.messagebox
from tkinter.ttk import *
from datetime import datetime
import random
import os
import csv
import time
from PIL import Image, ImageTk
from Date_data import months, months_to_num
from Names import names_males, names_females, surnames
from Student_data import majors, classes
from Employee_data import positions, salaries
from Address_data import streets, cities, states

# For some reason dir is defualted to my home dir, not the program dir
# os.chdir(r'codeProjects/misc-python-scripts/Data-Generator')

# The following variables pertain to the custom data option. They are declared in the main scope to make the custom
# data option function properly and allow the other generate functions to share data

attributes = []
user_choices = []
labels = []
custom_quantity = 0

# The following are the base functions for generating data.


def generate_dates(quantity, type_, form, year_start, year_end, sort):
    if type_ == "Full date":
        if form == "month day, year":
            rand_dates = []
            for i in range(quantity):
                year = random.randint(year_start, year_end)
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
            if sort == "Ascending":
                rand_dates.sort(key=lambda date_sort: datetime.strptime(date_sort, '%B %d; %Y'))
                return rand_dates
            elif sort == "Descending":
                rand_dates.sort(reverse=True, key=lambda date_sort: datetime.strptime(date_sort, '%B %d; %Y'))
                return rand_dates
            elif sort == "No sort":
                return rand_dates
        elif form == "mm/dd/yyyy":
            rand_dates = []
            for i in range(quantity):
                month = random.choice(months)
                numerical_month = months_to_num[month]
                year = random.randint(year_start, year_end)
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
            if sort == "Ascending":
                rand_dates.sort(key=lambda date_sort: datetime.strptime(date_sort, '%m/%d/%Y'))
                return rand_dates
            elif sort == "Descending":
                rand_dates.sort(reverse=True, key=lambda date_sort: datetime.strptime(date_sort, '%m/%d/%Y'))
                return rand_dates
            elif sort == "No sort":
                return rand_dates
        elif form == "day month year":
            rand_dates = []
            for i in range(quantity):
                month = random.choice(months)
                year = random.randint(year_start, year_end)
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
            if sort == "Ascending":
                rand_dates.sort(key=lambda date_sort: datetime.strptime(date_sort, '%d %B %Y'))
                return rand_dates
            elif sort == "Descending":
                rand_dates.sort(reverse=True, key=lambda date_sort: datetime.strptime(date_sort, '%d %B %Y'))
                return rand_dates
            elif sort == "No sort":
                return rand_dates
        elif form == "dd/mm/yyyy":
            rand_dates = []
            for i in range(quantity):
                month = random.choice(months)
                numerical_month = months_to_num[month]
                year = random.randint(year_start, year_end)
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
            if sort == "Ascending":
                rand_dates.sort(key=lambda date_sort: datetime.strptime(date_sort, '%d/%m/%Y'))
                return rand_dates
            elif sort == "Descending":
                rand_dates.sort(reverse=True, key=lambda date_sort: datetime.strptime(date_sort, '%d/%m/%Y'))
                return rand_dates
            elif sort == "No sort":
                return rand_dates
    elif type_ == "Months":
        rand_month = []
        for i in range(quantity):
            rand_month.append(random.choice(months))
        return rand_month
    elif type_ == "Years":
        rand_year = []
        for i in range(quantity):
            rand_year.append(random.randint(int(year_start), int(year_end)))
        return rand_year


def generate_numbers(quantity, option, range_start, range_end, round_var):
    if option == "Integers":
        integers = []
        for _ in range(quantity):
            integers.append(f"{random.randint(range_start, range_end)}")
        return integers
    elif option == "Decimals":
        floats = []
        for _ in range(quantity):
            num = random.uniform(range_start, range_end)
            floats.append(f"{round(num, round_var)}")
        return floats


def generate_names(quantity, option, is_called_in_custom=False):
    if option == "Male names":
        rand_name_males = random.sample(names_males, k=quantity)
        if is_called_in_custom:
            # This statement places a flag in the outputted list so other functions can find and use the data outputted
            # thus creating consistency within custom data. The flag is removed before writing to a file
            rand_name_males.insert(0, "names")
        return rand_name_males
    elif option == "Female names":
        rand_name_females = random.sample(names_females, k=quantity)
        if is_called_in_custom:
            rand_name_females.insert(0, "names")
        return rand_name_females
    elif option == "Mixed names":
        mixed_names = []
        rand_name_females = random.sample(names_females, k=quantity)
        rand_name_males = random.sample(names_males, k=quantity)
        for i in range(quantity):
            z = random.randint(0, 1)
            if z == 0:
                mixed_names.append(rand_name_females[i])
            else:
                mixed_names.append(rand_name_males[i])
        if is_called_in_custom:
            mixed_names.insert(0, "names")
        return mixed_names
    elif option == "Surnames":
        rand_name_surname = random.sample(surnames, k=quantity)
        if is_called_in_custom:
            rand_name_surname.insert(0, "names")
        if is_called_in_custom:
            rand_name_surname.insert(0, "names")
        return rand_name_surname
    elif option == "Full names male":
        rand_names_first = random.sample(names_males, k=quantity)
        rand_names_last = random.sample(surnames, k=quantity)
        full_names_male = []
        if is_called_in_custom:
            full_names_male.append("names")
        for i in range(quantity):
            full_names_male.append(f"{rand_names_first[i]} {rand_names_last[i]}")
        if is_called_in_custom:
            full_names_male.insert(0, "names")
        return full_names_male
    elif option == "Full names female":
        rand_names_first = random.sample(names_females, k=quantity)
        rand_names_last = random.sample(surnames, k=quantity)
        full_names_female = []
        for i in range(quantity):
            full_names_female.append(f"{rand_names_first[i]} {rand_names_last[i]}")
        if is_called_in_custom:
            full_names_female.insert(0, "names")
        return full_names_female
    elif option == "Full names mixed":
        rand_names_first_f = random.sample(names_females, k=quantity)
        rand_names_first_m = random.sample(names_males, k=quantity)
        rand_names_last = random.sample(surnames, k=quantity)
        mixed_full_names = []
        for i in range(quantity):
            z = random.randint(0, 1)
            if z == 0:
                first = rand_names_first_f[i]
            else:
                first = rand_names_first_m[i]
            mixed_full_names.append(f"{first} {rand_names_last[i]}")
        if is_called_in_custom:
            mixed_full_names.insert(0, "names")
        return mixed_full_names


def generate_dice_rolls(quantity, dice, is_called_in_custom=False):
    results = []
    if dice == 1:
        for i in range(quantity):
            if is_called_in_custom:
                results.append([random.randint(1, 6)])
            else:
                results.append([f"Set{i + 1}: ", random.randint(1, 6)])
        return results
    elif dice == 2:
        for i in range(quantity):
            if is_called_in_custom:
                results.append([random.randint(1, 6), random.randint(1, 6)])
            else:
                results.append([f"Set {i + 1}: ", random.randint(1, 6), random.randint(1, 6)])
        return results
    elif dice == 3:
        for i in range(quantity):
            if is_called_in_custom:
                results.append([random.randint(1, 6), random.randint(1, 6), random.randint(1, 6)])
            else:
                results.append([f"Set {i + 1}:", random.randint(1, 6), random.randint(1, 6), random.randint(1, 6)])
        return results
    elif dice == 4:
        for i in range(quantity):
            if is_called_in_custom:
                results.append([random.randint(1, 6), random.randint(1, 6), random.randint(1, 6), random.randint(1, 6)])
            else:
                results.append([f"Set {i + 1}:", random.randint(1, 6), random.randint(1, 6), random.randint(1, 6),
                                random.randint(1, 6)])
        return results
    elif dice == 5:
        for i in range(quantity):
            if is_called_in_custom:
                results.append([random.randint(1, 6), random.randint(1, 6), random.randint(1, 6), random.randint(1, 6),
                                random.randint(1, 6)])
            else:
                results.append([f"Set {i + 1}:", random.randint(1, 6), random.randint(1, 6), random.randint(1, 6),
                                random.randint(1, 6), random.randint(1, 6)])
        return results
    elif dice == 6:
        for i in range(quantity):
            if is_called_in_custom:
                results.append([random.randint(1, 6), random.randint(1, 6), random.randint(1, 6), random.randint(1, 6),
                                random.randint(1, 6), random.randint(1, 6)])
            else:
                results.append([f"Set {i + 1}:", random.randint(1, 6), random.randint(1, 6), random.randint(1, 6),
                                random.randint(1, 6), random.randint(1, 6), random.randint(1, 6)])
        return results


def generate_coin_tosses(quantity):
    total_tosses = []
    for i in range(quantity):
        toss = random.randint(0, 1)
        if toss == 0:
            total_tosses.append("Heads")
        else:
            total_tosses.append("Tails")
    return total_tosses


def generate_emails(quantity, is_called_in_custom=False):
    total_emails = []
    domains = ["gmail.com", "yahoo.com", "hotmail.com", "aol.com"]
    if is_called_in_custom:  # Here the function searches for a 'names' flag within the already
        # generated data (See generate_names)
        email_name_bank = []
        for attribute in attributes:
            if attribute[0] == "names":  # If found, the 'names' flag is removed and the flagged list becomes the name
                # bank that the function will pull from. This helps custom data stay consistent (see generate_names)
                attribute.remove("names")
                email_name_bank = attribute
        if len(email_name_bank[0].split(" ")) == 2:  # Checks if names in the names bank have a first and last name and
            # then generates accordingly
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
                    total_emails.append(f"{(email_name[0].lower()).strip()}{random.randint(100, 9999)}"
                                        f"@{random.choice(domains)}")
        else:
            for name in email_name_bank:
                var = random.randint(0, 1)
                if var == 0:
                    total_emails.append(f"{(name.lower()).strip()}{random.randint(100, 9999)}@{random.choice(domains)}")
                else:
                    total_emails.append(f"{random.randint(100, 9999)}{(name.lower()).strip()}@{random.choice(domains)}")
        return total_emails
    else:
        for i in range(quantity):
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


def generate_addresses(quantity, option):
    rand_addresses = []
    while True:
        if option == "Street address only":
            street = random.sample(streets, k=int(quantity))
            for i in range(int(quantity)):
                rand_addresses.append(f"{random.randint(1, 9999)} {street[i]}")

            return rand_addresses
        elif option == "Full address":
            street = random.sample(streets, k=int(quantity))
            city = random.sample(cities, k=int(quantity))
            state = random.choices(states, k=int(quantity))
            for i in range(int(quantity)):
                rand_addresses.append(f"{random.randint(1, 9999)} {street[i]}, {city[i]}, {state[i]}")
            return rand_addresses


def generate_phone_num(quantity):
    phone_numbers = []
    for i in range(quantity):
        phone_numbers.append(f"{random.randint(100, 999)}-{random.randint(100, 999)}-{random.randint(1000, 9999)}")
    return phone_numbers


def generate_true_false(quantity, statement, is_called_in_custom=False):
    output = []
    if is_called_in_custom:
        for i in range(quantity):
            n = random.randint(0, 1)
            if n == 0:
                output.append("True")
            else:
                output.append("False")
    else:
        for i in range(quantity):
            n = random.randint(0, 1)
            if n == 0:
                output.append([f"{statement}:", "True"])
            else:
                output.append([f"{statement}:", "False"])
        return output


def generate_user_database(quantity, data_bank, sample, sort):
    if sample == "Choices":
        values = random.choices(data_bank, k=int(quantity))
        if sort == "Ascending":
            values.sort()
            return values
        elif sort == "Descending":
            values.sort(reverse=True)
            return values
        elif sort == "No sort":
            return values
    elif sample == "Sample":
        values = random.sample(data_bank, k=int(quantity))
        if sort == "Ascending":
            values.sort()
            return values
        elif sort == "Descending":
            values.sort(reverse=True)
            return values
        elif sort == "No sort":
            return values


def generate_random_people(quantity, name_type, option_1, sub_option_1, option_2, option_3):
    people_names = []
    people_addresses = []
    people_emails = []
    people_numbers = []
    if name_type == "Male names only":
        rand_names_first_m = random.sample(names_males, k=int(quantity))
        rand_names_last = random.sample(surnames, k=int(quantity))
        for i in range(int(quantity)):
            people_names.append(f"{rand_names_first_m[i]}  {rand_names_last[i]}")
    elif name_type == "Female names only":
        rand_names_first_f = random.sample(names_females, k=int(quantity))
        rand_names_last = random.sample(surnames, k=int(quantity))
        for i in range(int(quantity)):
            people_names.append(f"{rand_names_first_f[i]}  {rand_names_last[i]}")
    elif name_type == "Mixed":
        rand_names_first_f = random.sample(names_females, k=int(quantity))
        rand_names_first_m = random.sample(names_males, k=int(quantity))
        rand_names_last = random.sample(surnames, k=int(quantity))
        for i in range(quantity):
            z = random.randint(0, 1)
            if z == 0:
                first = rand_names_first_f[i]
            else:
                first = rand_names_first_m[i]
            last = rand_names_last[i]
            people_names.append(f"{first} {last}")
    if option_1 == "Yes":
        if sub_option_1 == "Street address only":
            street = random.sample(streets, k=int(quantity))
            for i in range(int(quantity)):
                people_addresses.append(f"{random.randint(1, 9999)} {street[i]}")
        elif sub_option_1 == "Full address":
            street = random.sample(streets, k=int(quantity))
            city = random.sample(cities, k=int(quantity))
            for i in range(int(quantity)):
                people_addresses.append(f"{random.randint(1, 9999)} {street[i]}, {city[i]}, "
                                        f"{random.choice(states)}")
    if option_2 == "Yes":
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
    if option_3 == "Yes":
        for i in range(int(quantity)):
            people_numbers.append(f"{random.randint(100, 999)}-{random.randint(100, 999)}"
                                  f"-{random.randint(1000, 9999)}")
    people = []
    people_labels = []
    if people_names:
        people_labels.append("Name")
        for name in people_names:
            people.append([name])
    else:
        pass
    if people_addresses:
        people_labels.append("Address")
        i = 0
        for person in people:
            person.append(people_addresses[i])
            i += 1
    else:
        pass
    if people_emails:
        people_labels.append("Email")
        i = 0
        for person in people:
            person.append(people_emails[i])
            i += 1
    else:
        pass
    if people_numbers:
        people_labels.append("Phone Number")
        i = 0
        for person in people:
            person.append(people_numbers[i])
            i += 1
    else:
        pass
    people.insert(0, people_labels)
    return people


def generate_random_students(quantity, name_type, option_1, option_2, option_3):
    student_names = []
    student_gpa = []
    student_majors = []
    student_class = []
    if name_type == "Male names only":
        rand_names_first_m = random.sample(names_males, k=int(quantity))
        rand_names_last = random.sample(surnames, k=int(quantity))
        for i in range(int(quantity)):
            student_names.append(f"{rand_names_first_m[i]}  {rand_names_last[i]}")
    elif name_type == "Female names only":
        rand_names_first_f = random.sample(names_females, k=int(quantity))
        rand_names_last = random.sample(surnames, k=int(quantity))
        for i in range(int(quantity)):
            student_names.append(f"{rand_names_first_f[i]}  {rand_names_last[i]}")
    elif name_type == "Mixed":
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
    if option_1 == "Yes":
        for i in range(int(quantity)):
            student_gpa.append(round(random.uniform(2.0, 4.0), 2))
    if option_2 == "Yes":
        for i in range(int(quantity)):
            student_majors.append(random.choice(majors))
    if option_3 == "Yes":
        for i in range(int(quantity)):
            student_class.append(random.choice(classes))
    students = []
    student_labels = []
    if student_names:
        student_labels.append("Name")
        for student in student_names:
            students.append([student])
    if student_gpa:
        student_labels.append("GPA")
        i = 0
        for student in students:
            student.append(student_gpa[i])
            i += 1
    if student_majors:
        student_labels.append("Major")
        i = 0
        for student in students:
            student.append(student_majors[i])
            i += 1
    if student_class:
        student_labels.append("Class")
        i = 0
        for student in students:
            student.append(student_class[i])
            i += 1
    students.insert(0, student_labels)
    return students


def generate_random_employees(quantity, name_type, option_1, option_2, option_3):
    employee_names = []
    employee_salary = []
    employee_position = []
    employee_years_worked = []
    if name_type == "Male names only":
        rand_names_first_m = random.sample(names_males, k=int(quantity))
        rand_names_last = random.sample(surnames, k=int(quantity))
        for i in range(int(quantity)):
            employee_names.append(f"{rand_names_first_m[i]}  {rand_names_last[i]}")
    elif name_type == "Female names only":
        rand_names_first_f = random.sample(names_females, k=int(quantity))
        rand_names_last = random.sample(surnames, k=int(quantity))
        for i in range(int(quantity)):
            employee_names.append(f"{rand_names_first_f[i]}  {rand_names_last[i]}")
    elif name_type == "Mixed":
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
    if option_1 == "Yes":
        for i in range(int(quantity)):
            employee_salary.append(random.choice(salaries))
    if option_2 == "Yes":
        for i in range(int(quantity)):
            employee_position.append(random.choice(positions))
    if option_3 == "Yes":
        for i in range(int(quantity)):
            employee_years_worked.append(random.randint(1, 30))
    employees = []
    employee_labels = []
    if employee_names:
        employee_labels.append("Name")
        for employee in employee_names:
            employees.append([employee])
    else:
        pass
    if employee_salary:
        employee_labels.append("Salary")
        i = 0
        for employee in employees:
            employee.append(employee_salary[i])
            i += 1
    else:
        pass
    if employee_position:
        employee_labels.append("Position")
        i = 0
        for employee in employees:
            employee.append(employee_position[i])
            i += 1
    else:
        pass
    if employee_years_worked:
        employee_labels.append("Years Worked")
        i = 0
        for employee in employees:
            employee.append(employee_years_worked[i])
            i += 1
    else:
        pass
    employees.insert(0, employee_labels)
    return employees


def generate_card_draws(quantity, num_decks, sample):
    deck = ['Ace of Spades', 'Two of Spades', 'Three of Spades', 'Four of Spades', 'Five of Spades', 'Six of Spades',
            'Seven of Spades', 'Eight of Spades', 'Nine of Spades', 'Ten of Spades', 'Jack of Spades',
            'Queen of Spades', 'King of Spades', 'Ace of Hearts', 'Two of Hearts', 'Three of Hearts', 'Four of Hearts',
            'Five of Hearts', 'Six of Hearts', 'Seven of Hearts', 'Eight of Hearts', 'Nine of Hearts', 'Ten of Hearts',
            'Jack of Hearts', 'Queen of Hearts', 'King of Hearts', 'Ace of Clubs', 'Two of Clubs', 'Three of Clubs',
            'Four of Clubs', 'Five of Clubs', 'Six of Clubs', 'Seven of Clubs', 'Eight of Clubs', 'Nine of Clubs',
            'Ten of Clubs', 'Jack of Clubs', 'Queen of Clubs', 'King of Clubs', 'Ace of Diamonds', 'Two of Diamonds',
            'Three of Diamonds', 'Four of Diamonds', 'Five of Diamonds', 'Six of Diamonds', 'Seven of Diamonds',
            'Eight of Diamonds', 'Nine of Diamonds', 'Ten of Diamonds', 'Jack of Diamonds', 'Queen of Diamonds',
            'King of Diamonds']

    draw_deck = []

    for i in range(num_decks):
        for card in deck:
            draw_deck.append(card)

    if sample == 'Sample':
        drawn_cards = random.sample(draw_deck, k=quantity)
    else:
        drawn_cards = random.choices(draw_deck, k=quantity)

    return drawn_cards


option_counter = 0


def generate_custom_data():
    global option_counter
    global attributes
    global user_choices

    att_1 = None
    att_2 = None
    att_3 = None
    att_4 = None
    att_5 = None
    att_6 = None
    output = []
    funcs = {
        "Dates": create_dates_frame,
        "Names": create_names_frame,
        "Numbers": create_numbers_frame,
        "Emails": create_emails_frame,
        "Addresses": create_addresses_frame,
        "Phone Numbers": create_phone_num_frame,
        "User Data": create_user_database_frame,
        "True/False": create_true_false_frame,
        "Coin Tosses": create_coin_tosses_frame,
        "Card Draws": create_card_draws_frame,
        "Dice Rolls": create_dice_rolls_frame

    }
    custom_options_frame.tkraise()
    try:
        for widget in custom_options_frame.winfo_children():
            widget.destroy()
        funcs[user_choices[option_counter]](custom_options_frame, True)
        option_counter += 1
    except IndexError:
        option_counter = 0
        custom_data_path = filedialog.asksaveasfilename(filetypes=accepted_filetypes,
                                                        defaultextension=accepted_filetypes)

        # Up to this point, generate_custom_data has acquired a list of lists. In order to make working with the data
        # easier, the program now parses out each list and assigns it to its own variable.
        try:
            att_1 = attributes[0]
            if att_1[0] == "names":  # Ensures the 'names' flag is removed if it hasn't been
                # already (see generate_names)
                att_1.remove("names")
            att_2 = attributes[1]
            if att_2[0] == "names":
                att_2.remove("names")
            att_3 = attributes[2]
            if att_3[0] == "names":
                att_3.remove("names")
            att_4 = attributes[3]
            if att_4[0] == "names":
                att_4.remove("names")
            att_5 = attributes[4]
            if att_5[0] == "names":
                att_5.remove("names")
            att_6 = attributes[5]
            if att_6[0] == "names":
                att_6.remove("names")
        except IndexError:
            pass

        # In this for loop, each list is looped through and the corresponding values are put into their own list called
        # temp. This creates a single entry with all its attributes. Temp is then appended to the output list and temp
        # is reset. The output is a list of lists with each value being a single entry.

        for attribute in range(int(custom_quantity)):
            temp = []
            if att_1:
                temp.append(att_1[attribute])
            if att_2:
                temp.append(att_2[attribute])
            if att_3:
                temp.append(att_3[attribute])
            if att_4:
                temp.append(att_4[attribute])
            if att_5:
                temp.append(att_5[attribute])
            if att_6:
                temp.append(att_6[attribute])
            output.append(temp)
        output.insert(0, labels)
        write_file(output, custom_data_path)
        custom_frame.tkraise()


def write_file(in_list, write_path):
    try:
        with open(write_path, "w+", newline='') as csvFile:
            csv_writer = csv.writer(csvFile)
            for i in in_list:
                if type(i) is list:
                    csv_writer.writerow(i)
                else:
                    csv_writer.writerow([i])
    except PermissionError:
        tkinter.messagebox.showerror("File Save Error", "Could not save file")
    except FileNotFoundError:
        tkinter.messagebox.showerror("File Save Error", "File path not found")
    except OSError:
        tkinter.messagebox.showerror("File Save Error", "Could not save file")


root = Tk()
root.title("Data Generator")
if os.name == 'nt':
    icon = PhotoImage(file=r'Icons\main.png')
else:
    icon = PhotoImage(file=r'Icons/main.png')
root.iconphoto(False, icon)
root.geometry('550x420')

padingx = 20
padingy = 10
accepted_filetypes = [('Comma Separated Values *.csv', '*.csv'), ('Text Document *.txt', "*.txt")]

selections_frame = Frame(root)
dates_frame = Frame(root)
numbers_frame = Frame(root)
names_frame = Frame(root)
dice_rolls_frame = Frame(root)
coin_tosses_frame = Frame(root)
emails_frame = Frame(root)
addresses_frame = Frame(root)
phone_numbers_frame = Frame(root)
user_database_frame = Frame(root)
true_false_frame = Frame(root)
people_frame = Frame(root)
students_frame = Frame(root)
employee_frame = Frame(root)
card_draws_frame = Frame(root)
custom_frame = Frame(root)
custom_options_frame = Frame(root)

for frame in (selections_frame, dates_frame, numbers_frame, names_frame, dice_rolls_frame, coin_tosses_frame,
              emails_frame, addresses_frame, phone_numbers_frame, user_database_frame, true_false_frame, people_frame,
              students_frame, employee_frame, card_draws_frame, custom_frame, custom_options_frame):
    frame.grid(row=0, column=0, sticky='news')


if os.name == 'nt':
    dates_icon = ImageTk.PhotoImage(Image.open(r'Icons\Calendar-icon.png').resize((50, 50)))
    numbers_icon = ImageTk.PhotoImage(Image.open(r'Icons\Numbers-icon.png').resize((50, 50)))
    names_icon = ImageTk.PhotoImage(Image.open(r'Icons\Hello-My-Name-Is-Rupert-icon.png').resize((50, 50)))
    dice_rolls_icon = ImageTk.PhotoImage(Image.open(r'Icons\Dice-icon.png').resize((50, 50)))
    coin_tosses_icon = ImageTk.PhotoImage(Image.open(r'Icons\coin-icon.png').resize((50, 50)))
    emails_icon = ImageTk.PhotoImage(Image.open(r'Icons\Mail-icon.png').resize((50, 50)))
    addresses_icon = ImageTk.PhotoImage(Image.open(r'Icons\Address-Book-icon.png').resize((50, 50)))
    phone_num_icon = ImageTk.PhotoImage(Image.open(r'Icons\Phonebook-icon.png').resize((50, 50)))
    user_database_icon = ImageTk.PhotoImage(Image.open(r'Icons\Letters-icon.png').resize((50, 50)))
    true_false_icon = ImageTk.PhotoImage(Image.open(r'Icons\sign-check-icon.png').resize((50, 50)))
    people_icon = ImageTk.PhotoImage(Image.open(r'Icons\Person-Male-Light-icon.png').resize((50, 50)))
    students_icon = ImageTk.PhotoImage(Image.open(r'Icons\Student-Male-icon.png').resize((50, 50)))
    employees_icon = ImageTk.PhotoImage(Image.open(r'Icons\Office-Customer-Male-Light-icon.png').resize((50, 50)))
    card_draws_icon = ImageTk.PhotoImage(Image.open(r'Icons\Apps-Game-Cards-icon.png').resize((50, 50)))
    custom_icon = ImageTk.PhotoImage(Image.open(r'Icons\custom-reports-icon.png').resize((50, 50)))
else:
    dates_icon = ImageTk.PhotoImage(Image.open(r'Icons/Calendar-icon.png').resize((50, 50)))
    numbers_icon = ImageTk.PhotoImage(Image.open(r'Icons/Numbers-icon.png').resize((50, 50)))
    names_icon = ImageTk.PhotoImage(Image.open(r'Icons/Hello-My-Name-Is-Rupert-icon.png').resize((50, 50)))
    dice_rolls_icon = ImageTk.PhotoImage(Image.open(r'Icons/Dice-icon.png').resize((50, 50)))
    coin_tosses_icon = ImageTk.PhotoImage(Image.open(r'Icons/coin-icon.png').resize((50, 50)))
    emails_icon = ImageTk.PhotoImage(Image.open(r'Icons/Mail-icon.png').resize((50, 50)))
    addresses_icon = ImageTk.PhotoImage(Image.open(r'Icons/Address-Book-icon.png').resize((50, 50)))
    phone_num_icon = ImageTk.PhotoImage(Image.open(r'Icons/Phonebook-icon.png').resize((50, 50)))
    user_database_icon = ImageTk.PhotoImage(Image.open(r'Icons/Letters-icon.png').resize((50, 50)))
    true_false_icon = ImageTk.PhotoImage(Image.open(r'Icons/sign-check-icon.png').resize((50, 50)))
    people_icon = ImageTk.PhotoImage(Image.open(r'Icons/Person-Male-Light-icon.png').resize((50, 50)))
    students_icon = ImageTk.PhotoImage(Image.open(r'Icons/Student-Male-icon.png').resize((50, 50)))
    employees_icon = ImageTk.PhotoImage(Image.open(r'Icons/Office-Customer-Male-Light-icon.png').resize((50, 50)))
    card_draws_icon = ImageTk.PhotoImage(Image.open(r'Icons/Apps-Game-Cards-icon.png').resize((50, 50)))
    custom_icon = ImageTk.PhotoImage(Image.open(r'Icons/custom-reports-icon.png').resize((50, 50)))


def return_to_home():
    selections_frame.tkraise()
    root.geometry('550x420')


"""The following functions are set up in a way so that the custom data option can use them to get the arguments 
needed for the generation functions. Note: only options that are able to be included in custom data 
i.e functions that output only one type of value, are set up like this. Random people, students, and employees are not 
set up like this."""


def create_dates_frame(build_frame, is_called_in_custom=False):
    global dates_icon
    global custom_quantity
    global attributes

    # noinspection PyUnusedLocal
    def show_alt_options_dates(*args):
        if date_type.get() == "Full date":
            date_format_label.grid(row=2, column=2, padx=5, sticky=E)
            date_format_select.grid(row=2, column=3, padx=5)
            date_rangex.grid(row=3, column=2, padx=5, sticky=E)
            date_rangex_entry.grid(row=3, column=3, padx=5, sticky=W)
            date_rangey.grid(row=4, column=2, padx=5, sticky=E)
            date_rangey_entry.grid(row=4, column=3, padx=5, sticky=W)
        elif date_type.get() == "Years":
            date_format_label.grid_forget()
            date_format_select.grid_forget()
            date_rangex.grid(row=3, column=2, sticky=E)
            date_rangex_entry.grid(row=3, column=3, sticky=W)
            date_rangey.grid(row=4, column=2, sticky=E)
            date_rangey_entry.grid(row=4, column=3, sticky=W)
        else:
            date_format_label.grid_forget()
            date_format_select.grid_forget()
            date_rangex.grid_forget()
            date_rangex_entry.grid_forget()
            date_rangey.grid_forget()
            date_rangey_entry.grid_forget()

    date_type = StringVar()
    date_type.set("")

    format_type = StringVar()
    format_type.set("")

    sort_type = StringVar()
    sort_type.set("")

    date_error = StringVar()
    date_done = StringVar()

    def dates_generate_command():
        date_done.set("")
        if is_called_in_custom:
            q = custom_quantity
        else:
            q = dates_quantity_entry.get()
        typ = date_type.get()
        ys = date_rangex_entry.get()
        ye = date_rangey_entry.get()
        form = format_type.get()
        sort = sort_type.get()

        if q == "":
            date_error.set("Please fill in all options")
            return
        elif typ == "":
            date_error.set("Please fill in all options")
            return
        elif ys == "":
            if typ == "Months":
                pass
            else:
                date_error.set("Please fill in all options")
                return
        elif ye == "":
            if typ == "Months":
                pass
            else:
                date_error.set("Please fill in all options")
                return
        elif form == "":
            if typ == "Months":
                pass
            elif typ == "Years":
                pass
            else:
                date_error.set("Please fill in all options")
                return
        elif sort == "":
            date_error.set("Please fill in all options")
            return

        try:
            q = int(q)
            date_error.set("")
        except ValueError:
            date_error.set("Invalid input for quantity")
            return

        if typ == "Months":
            pass
        else:
            try:
                ys = int(ys)
                ye = int(ye)
                random.randint(ys, ye)
                date_error.set("")
            except ValueError:
                date_error.set("Invalid input for year ranges")
                return

        out = generate_dates(q, typ, form, ys, ye, sort)
        if is_called_in_custom:
            attributes.append(out)
            generate_custom_data()
        else:
            save_path = filedialog.asksaveasfilename(filetypes=accepted_filetypes, defaultextension=accepted_filetypes)
            write_file(out, save_path)
            date_done.set("DONE")

    dates_intro = Label(build_frame, image=dates_icon, font=11)
    dates_intro.grid(row=0, column=1, pady=10)

    if is_called_in_custom:
        pass
    else:
        dates_quantity_label = Label(build_frame, text="Quantity: ")
        dates_quantity_entry = Entry(build_frame)
        dates_quantity_label.grid(row=1, column=0, padx=padingx, pady=padingy, sticky=E)
        dates_quantity_entry.grid(row=1, column=1, padx=padingx, pady=padingy, sticky=W)

    date_type_label = Label(build_frame, text="Type: ")
    date_type_select = Combobox(build_frame, textvariable=date_type, values=('Full date', 'Months', 'Years'),
                                state='readonly')

    date_type_label.grid(row=2, column=0, padx=padingx, pady=padingy, sticky=E)
    date_type_select.grid(row=2, column=1, padx=padingx, pady=padingy)
    date_type_select.bind('<<ComboboxSelected>>', show_alt_options_dates)

    date_format_label = Label(build_frame, text='Format: ')
    date_format_select = Combobox(build_frame, textvariable=format_type, state='readonly', values=('month day, year',
                                                                                                   'mm/dd/yyyy',
                                                                                                   'day month year',
                                                                                                   'dd/mm/yyyy'))

    date_rangex = Label(build_frame, text="Year Start: ")
    date_rangex_entry = Entry(build_frame)

    date_rangey = Label(build_frame, text="Year End: ")
    date_rangey_entry = Entry(build_frame)

    sort_type_label = Label(build_frame, text='Sorting: ')
    sort_type_select = Combobox(build_frame, textvariable=sort_type, values=('Ascending', 'Descending', 'No sort'),
                                state='readonly')

    sort_type_label.grid(row=3, column=0, padx=padingx, pady=padingy, sticky=E)
    sort_type_select.grid(row=3, column=1, padx=padingx, pady=padingy)

    if is_called_in_custom:
        dates_generate_button = Button(build_frame, text="Confirm Selection", command=dates_generate_command)
        dates_generate_button.grid(row=4, column=1, padx=padingx, pady=padingy)

        dates_back = Button(build_frame, text="Change Selection", command=back_out)
        dates_back.grid(row=4, column=0, padx=padingx, pady=padingy)

        dates_error_label = Label(build_frame, textvariable=date_error, foreground="red")
        dates_error_label.grid(row=5, column=1, padx=padingx, pady=padingy)
    else:
        dates_generate_button = Button(build_frame, text="Generate", command=dates_generate_command)
        dates_generate_button.grid(row=4, column=1, padx=padingx, pady=padingy)

        dates_back = Button(build_frame, text="Back", command=return_to_home)
        dates_back.grid(row=4, column=0, padx=padingx, pady=padingy)

        dates_error_label = Label(build_frame, textvariable=date_error, foreground="red")
        dates_error_label.grid(row=5, column=1, padx=padingx, pady=padingy)

        dates_done_label = Label(build_frame, textvariable=date_done)
        dates_done_label.grid(row=6, column=1, padx=padingx, pady=padingy)


create_dates_frame(dates_frame)


def create_numbers_frame(build_frame, is_called_in_custom=False):
    global custom_quantity
    global attributes
    global numbers_icon

    # noinspection PyUnusedLocal
    def show_alt_options_numbers(*args):
        if number_type.get() == "Decimals":
            round_label.grid(row=2, column=3, sticky=E)
            round_entry.grid(row=2, column=4, sticky=W)
        else:
            round_label.grid_forget()
            round_entry.grid_forget()

    def numbers_generate_command():
        number_done.set("")
        if is_called_in_custom:
            q = custom_quantity
        else:
            q = numbers_quantity_entry.get()
        num_typ = number_type.get()
        rstrt = numbers_rangex_entry.get()
        rend = numbers_rangey_entry.get()
        rou = round_entry.get()

        if q == "":
            number_error.set("Please fill in all options")
            return
        elif num_typ == "":
            number_error.set("Please fill in all options")
            return
        elif rstrt == "":
            number_error.set("Please fill in all options")
            return
        elif rend == "":
            number_error.set("Please fill in all options")
            return
        elif rou == "":
            if num_typ == "Integers":
                pass
            elif num_typ == "Decimals":
                number_error.set("Please fill in all options")
                return

        try:
            q = int(q)
            number_error.set("")
        except ValueError:
            number_error.set("Invalid input for quantity")
            return
        try:
            if num_typ == "Decimals":
                rou = int(rou)
            rstrt = int(rstrt)
            rend = int(rend)
            random.randint(rstrt, rend)
            number_error.set("")
        except ValueError:
            number_error.set("Invalid input for ranges")
            return

        out = generate_numbers(q, num_typ, rstrt, rend, rou)
        if is_called_in_custom:
            attributes.append(out)
            generate_custom_data()
        else:
            save_path = filedialog.asksaveasfilename(filetypes=accepted_filetypes, defaultextension=accepted_filetypes)
            write_file(out, save_path)
            number_done.set("DONE")

    number_type = StringVar()
    number_type.set("")

    number_error = StringVar()
    number_done = StringVar()

    numbers_intro = Label(build_frame, image=numbers_icon)
    numbers_intro.grid(row=0, column=1, pady=10)
    if is_called_in_custom:
        pass
    else:
        numbers_quantity_label = Label(build_frame, text="Quantity: ")
        numbers_quantity_entry = Entry(build_frame)
        numbers_quantity_label.grid(row=1, column=0, padx=padingx, pady=padingy, sticky=E)
        numbers_quantity_entry.grid(row=1, column=1, padx=padingx, pady=padingy, sticky=W)

    number_type_label = Label(build_frame, text="Select name type:")
    number_type_label.grid(row=2, column=0, padx=padingx, pady=padingy, sticky=E)

    number_type_select = Combobox(build_frame, textvariable=number_type, values=('Integers', 'Decimals'),
                                  state='readonly')
    number_type_select.grid(row=2, column=1, padx=padingx, pady=padingy)
    number_type_select.bind('<<ComboboxSelected>>', show_alt_options_numbers)

    numbers_rangex = Label(build_frame, text="Range Start:")
    numbers_rangex.grid(row=3, column=0, padx=padingx, pady=padingy, sticky=E)

    numbers_rangex_entry = Entry(build_frame)
    numbers_rangex_entry.grid(row=3, column=1, padx=padingx, pady=padingy, sticky=W)

    numbers_rangey = Label(build_frame, text="Range End:")
    numbers_rangey.grid(row=4, column=0, padx=padingx, pady=padingy, sticky=E)

    numbers_rangey_entry = Entry(build_frame)
    numbers_rangey_entry.grid(row=4, column=1, padx=padingx, pady=padingy, sticky=W)

    round_label = Label(build_frame, text="Places to round:")
    round_entry = Entry(build_frame)

    if is_called_in_custom:
        numbers_generate_button = Button(build_frame, text="Confirm Selection", command=numbers_generate_command)
        numbers_generate_button.grid(row=5, column=1, padx=padingx, pady=padingy)
        numbers_back = Button(build_frame, text="Change Selection", command=back_out)
        numbers_back.grid(row=5, column=0, padx=padingx, pady=padingy)
        numbers_error_label = Label(build_frame, textvariable=number_error, foreground="red")
        numbers_error_label.grid(row=6, column=1, padx=padingx, pady=padingy)

    else:
        numbers_generate_button = Button(build_frame, text="Generate", command=numbers_generate_command)
        numbers_generate_button.grid(row=5, column=1, padx=padingx, pady=padingy)

        numbers_back = Button(build_frame, text="Back", command=return_to_home)
        numbers_back.grid(row=5, column=0, padx=padingx, pady=padingy)

        numbers_error_label = Label(build_frame, textvariable=number_error, foreground="red")
        numbers_error_label.grid(row=6, column=1, padx=padingx, pady=padingy)

        numbers_done_label = Label(build_frame, textvariable=number_done)
        numbers_done_label.grid(row=7, column=1, padx=padingx, pady=padingy)


create_numbers_frame(numbers_frame, False)


def create_names_frame(build_frame, is_called_in_custom=False):
    global custom_quantity
    global attributes
    global names_icon

    def names_generate_command():
        names_done.set("")
        if is_called_in_custom:
            q = custom_quantity
        else:
            q = names_quantity_entry.get()
        nam_typ = names_type.get()

        if q == "":
            names_error.set("Please fill in all options")
            return
        elif nam_typ == "":
            names_error.set("Please fill in all options")
            return

        try:
            q = int(q)
            names_error.set("")
        except ValueError:
            names_error.set("Invalid input for quantity")
            return

        if q > 999:
            names_error.set("Max number of names is 999")
            return

        out = generate_names(q, nam_typ, is_called_in_custom=is_called_in_custom)
        if is_called_in_custom:
            attributes.append(out)
            generate_custom_data()
        else:
            save_path = filedialog.asksaveasfilename(filetypes=accepted_filetypes, defaultextension=accepted_filetypes)
            write_file(out, save_path)
            names_done.set("DONE")

    names_error = StringVar()
    names_done = StringVar()

    names_type = StringVar()
    names_type.set("")

    names_intro = Label(build_frame, image=names_icon)
    names_intro.grid(row=0, column=1, pady=10)

    if is_called_in_custom:
        pass
    else:
        names_quantity_label = Label(build_frame, text="Quantity: ")
        names_quantity_entry = Entry(build_frame)
        names_quantity_label.grid(row=1, column=0, padx=padingx, pady=padingy, sticky=E)
        names_quantity_entry.grid(row=1, column=1, padx=padingx, pady=padingy, sticky=W)

    names_type_label = Label(build_frame, text="Select name type:")
    names_type_label.grid(row=2, column=0, padx=padingx, pady=padingy, sticky=E)

    names_type_select = Combobox(build_frame, textvariable=names_type, state='readonly', values=('Male names',
                                                                                                 'Female names',
                                                                                                 'Mixed names',
                                                                                                 'Surnames',
                                                                                                 'Full names male',
                                                                                                 'Full names female',
                                                                                                 'Full names mixed'))
    names_type_select.grid(row=2, column=1, padx=padingx, pady=padingy)

    if is_called_in_custom:
        names_generate_button = Button(build_frame, text="Confirm Selection", command=names_generate_command)
        names_generate_button.grid(row=3, column=1, padx=padingx, pady=padingy)

        names_back = Button(build_frame, text="Change Selection", command=back_out)
        names_back.grid(row=3, column=0, padx=padingx, pady=padingy)

        names_error_label = Label(build_frame, textvariable=names_error, foreground="red")
        names_error_label.grid(row=4, column=1, padx=padingx, pady=padingy)

    else:
        names_generate_button = Button(build_frame, text="Generate", command=names_generate_command)
        names_generate_button.grid(row=3, column=1, padx=padingx, pady=padingy)

        names_back = Button(build_frame, text="Back", command=return_to_home)
        names_back.grid(row=3, column=0, padx=padingx, pady=padingy)

        names_error_label = Label(build_frame, textvariable=names_error, foreground="red")
        names_error_label.grid(row=4, column=1, padx=padingx, pady=padingy)

        names_done_label = Label(build_frame, textvariable=names_done)
        names_done_label.grid(row=5, column=1, padx=padingx, pady=padingy)


create_names_frame(names_frame, False)


def create_dice_rolls_frame(build_frame, is_called_in_custom=False):
    global custom_quantity
    global attributes
    global dice_rolls_icon

    def dice_rolls_generate_command():
        dice_done.set("")
        if is_called_in_custom:
            q = custom_quantity
        else:
            q = dice_rolls_quantity_entry.get()
        amnt = dice_rolls_amount.get()

        if q == "":
            dice_error.set("Please fill in all options")
            return

        try:
            q = int(q)
            dice_error.set("")
        except ValueError:
            dice_error.set("Invalid input for quantity")
            return

        out = generate_dice_rolls(q, amnt, is_called_in_custom=is_called_in_custom)
        if is_called_in_custom:
            attributes.append(out)
            generate_custom_data()
        else:
            save_path = filedialog.asksaveasfilename(filetypes=accepted_filetypes, defaultextension=accepted_filetypes)
            write_file(out, save_path)
            dice_done.set("DONE")

    def single_roll():
        num_dice = single_roll_amount.get()
        single_roll_text.set("   Rolling...   ")  # Whitespace needed to cover up previous roll
        dice_rolls_frame.update_idletasks()
        time.sleep(0.8)
        if num_dice == 1:
            single_roll_text.set(f"{random.randint(1, 6)}")
        elif num_dice == 2:
            single_roll_text.set(f"{random.randint(1, 6)}, {random.randint(1, 6)}")
        elif num_dice == 3:
            single_roll_text.set(f"{random.randint(1, 6)}, {random.randint(1, 6)}, {random.randint(1, 6)}")
        elif num_dice == 4:
            single_roll_text.set(f"{random.randint(1, 6)}, {random.randint(1, 6)}, {random.randint(1, 6)}, "
                                 f"{random.randint(1, 6)}")
        elif num_dice == 5:
            single_roll_text.set(f"{random.randint(1, 6)}, {random.randint(1, 6)}, {random.randint(1, 6)}, "
                                 f"{random.randint(1, 6)}, {random.randint(1, 6)}")
        elif num_dice == 6:
            single_roll_text.set(f"{random.randint(1, 6)}, {random.randint(1, 6)}, {random.randint(1, 6)}, "
                                 f"{random.randint(1, 6)}, {random.randint(1, 6)}, {random.randint(1, 6)}")

    dice_error = StringVar()
    dice_done = StringVar()
    dice_rolls_amount = IntVar()
    dice_rolls_amount.set(1)

    dice_rolls_intro = Label(build_frame, image=dice_rolls_icon)
    dice_rolls_intro.grid(row=0, column=1, pady=10)

    if is_called_in_custom:
        pass
    else:
        dice_rolls_quantity_label = Label(build_frame, text="Quantity: ")
        dice_rolls_quantity_entry = Entry(build_frame)
        dice_rolls_quantity_label.grid(row=1, column=0, padx=padingx, pady=padingy, sticky=E)
        dice_rolls_quantity_entry.grid(row=1, column=1, padx=padingx, pady=padingy, sticky=W)

    dice_amount_label = Label(build_frame, text="Number of dice: ")
    dice_amount_select = Combobox(build_frame, textvariable=dice_rolls_amount, values=(1, 2, 3, 4, 5, 6),
                                  state='readonly')
    dice_amount_label.grid(row=2, column=0, padx=padingx, pady=padingy, sticky=E)
    dice_amount_select.grid(row=2, column=1, padx=padingx, pady=padingy)

    if is_called_in_custom:
        dice_roll_generate_button = Button(build_frame, text="Confirm Selection", command=dice_rolls_generate_command)
        dice_roll_generate_button.grid(row=3, column=1, padx=padingx, pady=padingy)

        dice_roll_back = Button(build_frame, text="Change Selection", command=back_out)
        dice_roll_back.grid(row=3, column=0, padx=padingx, pady=padingy)

        dice_roll_error_label = Label(build_frame, textvariable=dice_error, foreground="red")
        dice_roll_error_label.grid(row=4, column=1, padx=padingx, pady=padingy)
    else:
        dice_roll_generate_button = Button(build_frame, text="Generate", command=dice_rolls_generate_command)
        dice_roll_generate_button.grid(row=3, column=1, padx=padingx, pady=padingy)

        dice_roll_back = Button(build_frame, text="Back", command=return_to_home)
        dice_roll_back.grid(row=3, column=0, padx=padingx, pady=padingy)

        dice_roll_error_label = Label(build_frame, textvariable=dice_error, foreground="red")
        dice_roll_error_label.grid(row=4, column=1, padx=padingx, pady=padingy)

        dice_roll_done_label = Label(build_frame, textvariable=dice_done)
        dice_roll_done_label.grid(row=5, column=1, padx=padingx, pady=padingy)

        single_roll_text = StringVar()
        single_roll_text.set("")

        single_roll_amount = IntVar()
        single_roll_amount.set(1)

        single_roll_button = Button(build_frame, text="Single Roll", command=single_roll)
        single_roll_button.grid(row=6, column=0, padx=padingx, pady=padingy)

        single_roll_select = Combobox(build_frame, textvariable=single_roll_amount, values=(1, 2, 3, 4, 5, 6),
                                      state='readonly')

        single_roll_select.grid(row=6, column=1, padx=padingx, pady=padingy)

        single_roll_label = Label(build_frame, textvariable=single_roll_text)
        single_roll_label.grid(row=7, column=1)


create_dice_rolls_frame(dice_rolls_frame, False)


def create_coin_tosses_frame(build_frame, is_called_in_custom=False):
    global custom_quantity
    global attributes
    global coin_tosses_icon

    def coin_tosses_generate_command():
        coin_done.set("")
        if is_called_in_custom:
            q = custom_quantity
        else:
            q = coin_tosses_quantity_entry.get()

        if q == "":
            coin_error.set("Please fill in all options")
            return

        try:
            q = int(q)
            coin_error.set("")
        except ValueError:
            coin_error.set("Invalid input for quantity")
            return

        out = generate_coin_tosses(q)
        if is_called_in_custom:
            attributes.append(out)
            generate_custom_data()
        else:
            save_path = filedialog.asksaveasfilename(filetypes=accepted_filetypes, defaultextension=accepted_filetypes)
            write_file(out, save_path)
            coin_done.set("DONE")

    def single_toss():
        single_toss_text.set("Tossing...")
        coin_tosses_frame.update_idletasks()
        time.sleep(0.8)
        toss = random.randint(0, 1)
        if toss == 0:
            single_toss_text.set("Heads")
        else:
            single_toss_text.set("Tails")

    coin_error = StringVar()
    coin_done = StringVar()

    coin_tosses_intro = Label(build_frame, image=coin_tosses_icon)
    coin_tosses_intro.grid(row=0, column=1, pady=10)

    if is_called_in_custom:
        pass
    else:
        coin_tosses_quantity_label = Label(build_frame, text="Quantity:")
        coin_tosses_quantity_entry = Entry(build_frame)
        coin_tosses_quantity_label.grid(row=1, column=0, padx=padingx, pady=padingy, sticky=E)
        coin_tosses_quantity_entry.grid(row=1, column=1, padx=padingx, pady=padingy, sticky=W)

    if is_called_in_custom:
        coin_tosses_generate_button = Button(build_frame, text="Confirm Selection",
                                             command=coin_tosses_generate_command)
        coin_tosses_generate_button.grid(row=2, column=1, padx=padingx, pady=padingy)

        coin_tosses_back = Button(build_frame, text="Change Selection", command=back_out)
        coin_tosses_back.grid(row=2, column=0, padx=padingx, pady=padingy)

        coin_toss_error_label = Label(build_frame, textvariable=coin_error, foreground="red")
        coin_toss_error_label.grid(row=3, column=1, padx=padingx, pady=padingy)
    else:
        coin_tosses_generate_button = Button(build_frame, text="Generate", command=coin_tosses_generate_command)
        coin_tosses_generate_button.grid(row=2, column=1, padx=padingx, pady=padingy)

        coin_tosses_back = Button(build_frame, text="Back", command=return_to_home)
        coin_tosses_back.grid(row=2, column=0, padx=padingx, pady=padingy)

        coin_tosses_error_label = Label(build_frame, textvariable=coin_error, foreground="red")
        coin_tosses_error_label.grid(row=3, column=1, padx=padingx, pady=padingy)
        coin_tosses_done_label = Label(build_frame, textvariable=coin_done)
        coin_tosses_done_label.grid(row=4, column=1, padx=padingx, pady=padingy)

        single_toss_text = StringVar()
        single_toss_text.set("")

        single_toss_button = Button(build_frame, text="Single Toss", command=single_toss)
        single_toss_button.grid(row=5, column=0)

        single_toss_label = Label(build_frame, textvariable=single_toss_text)
        single_toss_label.grid(row=5, column=1)


create_coin_tosses_frame(coin_tosses_frame, False)


def create_emails_frame(build_frame, is_called_in_custom=False):
    global custom_quantity
    global attributes
    global emails_icon

    def emails_generate_command():
        email_done.set("")
        if is_called_in_custom:
            q = custom_quantity
        else:
            q = emails_quantity_entry.get()

        if q == "":
            email_error.set("Please fill in all options")
            return

        try:
            q = int(q)
            email_error.set("")
        except ValueError:
            email_error.set("Invalid input for quantity")
            return

        out = generate_emails(q, is_called_in_custom=is_called_in_custom)
        if is_called_in_custom:
            attributes.append(out)
            generate_custom_data()
        else:
            save_path = filedialog.asksaveasfilename(filetypes=accepted_filetypes, defaultextension=accepted_filetypes)
            write_file(out, save_path)
            email_done.set("DONE")

    email_error = StringVar()
    email_done = StringVar()

    emails_intro = Label(build_frame, image=emails_icon)
    emails_intro.grid(row=0, column=1, pady=10)

    if is_called_in_custom:
        pass
    else:
        emails_quantity_label = Label(build_frame, text="Quantity: ")
        emails_quantity_entry = Entry(build_frame)

        emails_quantity_label.grid(row=1, column=0, padx=padingx, pady=padingy, sticky=E)
        emails_quantity_entry.grid(row=1, column=1, padx=padingx, pady=padingy, sticky=W)

    if is_called_in_custom:
        emails_generate_button = Button(build_frame, text="Confirm Selection", command=emails_generate_command)
        emails_generate_button.grid(row=2, column=1, padx=padingx, pady=padingy)

        emails_back = Button(build_frame, text="Change Selection", command=back_out)
        emails_back.grid(row=2, column=0, padx=padingx, pady=padingy)

        emails_error_label = Label(build_frame, textvariable=email_error, foreground="red")
        emails_error_label.grid(row=3, column=1, padx=padingx, pady=padingy)
    else:
        emails_generate_button = Button(build_frame, text="Generate", command=emails_generate_command)
        emails_generate_button.grid(row=2, column=1, padx=padingx, pady=padingy)

        emails_back = Button(build_frame, text="Back", command=return_to_home)
        emails_back.grid(row=2, column=0, padx=padingx, pady=padingy)

        emails_error_label = Label(build_frame, textvariable=email_error, foreground="red")
        emails_error_label.grid(row=3, column=1, padx=padingx, pady=padingy)
        emails_done_label = Label(build_frame, textvariable=email_done)
        emails_done_label.grid(row=4, column=1, padx=padingx, pady=padingy)


create_emails_frame(emails_frame, False)


def create_addresses_frame(build_frame, is_called_in_custom=False):
    global custom_quantity
    global attributes
    global addresses_icon

    def addresses_generate_command():
        address_done.set("")
        if is_called_in_custom:
            q = custom_quantity
        else:
            q = addresses_quantity_entry.get()
        o = address_type.get()

        if q == "":
            address_error.set("Please fill in all options")
            return
        elif o == "":
            address_error.set("Please fill in all options")
            return

        try:
            q = int(q)
            address_error.set("")
        except ValueError:
            address_error.set("Invalid input for quantity")
            return

        if q > 999:
            address_error.set("Max number of names is 999")
            return
        out = generate_addresses(q, o)
        if is_called_in_custom:
            attributes.append(out)
            generate_custom_data()
        else:
            save_path = filedialog.asksaveasfilename(filetypes=accepted_filetypes, defaultextension=accepted_filetypes)
            write_file(out, save_path)
            address_done.set("DONE")

    address_error = StringVar()
    address_done = StringVar()

    address_type = StringVar()
    address_type.set("")

    addresses_intro = Label(build_frame, image=addresses_icon)
    addresses_intro.grid(row=0, column=1, pady=10)

    if is_called_in_custom:
        pass
    else:
        addresses_quantity_label = Label(build_frame, text="Quantity: ")
        addresses_quantity_entry = Entry(build_frame)
        addresses_quantity_label.grid(row=1, column=0, padx=padingx, pady=padingy, sticky=E)
        addresses_quantity_entry.grid(row=1, column=1, padx=padingx, pady=padingy, sticky=W)

    addresses_type_label = Label(build_frame, text="Select address type:")
    addresses_type_label.grid(row=2, column=0, padx=padingx, pady=padingy, sticky=E)

    addresses_type_select = Combobox(build_frame, textvariable=address_type, values=('Street address only',
                                                                                     'Full address'), state='readonly')
    addresses_type_select.grid(row=2, column=1, padx=padingx, pady=padingy)

    if is_called_in_custom:
        addresses_generate_button = Button(build_frame, text="Confirm Selection", command=addresses_generate_command)
        addresses_generate_button.grid(row=3, column=1, padx=padingx, pady=padingy)
        addresses_back = Button(build_frame, text="Change Selection", command=back_out)
        addresses_back.grid(row=3, column=0, padx=padingx, pady=padingy)
        addresses_error_label = Label(build_frame, textvariable=address_error, foreground="red")
        addresses_error_label.grid(row=4, column=1, padx=padingx, pady=padingy)
    else:
        addresses_generate_button = Button(build_frame, text="Generate", command=addresses_generate_command)
        addresses_generate_button.grid(row=3, column=1, padx=padingx, pady=padingy)

        addresses_back = Button(build_frame, text="Back", command=return_to_home)
        addresses_back.grid(row=3, column=0, padx=padingx, pady=padingy)

        addresses_error_label = Label(build_frame, textvariable=address_error, foreground="red")
        addresses_error_label.grid(row=4, column=1, padx=padingx, pady=padingy)
        addresses_done_label = Label(build_frame, textvariable=address_done)
        addresses_done_label.grid(row=5, column=1, padx=padingx, pady=padingy)


create_addresses_frame(addresses_frame, False)


def create_phone_num_frame(build_frame, is_called_in_custom=False):
    global phone_num_icon
    global custom_quantity
    global attributes

    def phone_num_generate_command():
        phone_done.set("")
        if is_called_in_custom:
            q = custom_quantity
        else:
            q = phone_num_quantity_entry.get()

        if q == "":
            phone_error.set("Please fill in all options")
            return

        try:
            q = int(q)
            phone_error.set("")
        except ValueError:
            phone_error.set("Invalid input for quantity")
            return
        out = generate_phone_num(q)
        if is_called_in_custom:
            attributes.append(out)
            generate_custom_data()
        else:
            save_path = filedialog.asksaveasfilename(filetypes=accepted_filetypes, defaultextension=accepted_filetypes)
            write_file(out, save_path)
            phone_done.set("DONE")

    phone_error = StringVar()
    phone_done = StringVar()

    phone_num_intro = Label(build_frame, image=phone_num_icon)
    phone_num_intro.grid(row=0, column=1, pady=10)

    if is_called_in_custom:
        pass
    else:
        phone_num_quantity_label = Label(build_frame, text="Quantity: ")
        phone_num_quantity_entry = Entry(build_frame)
        phone_num_quantity_label.grid(row=1, column=0, padx=padingx, pady=padingy, sticky=E)
        phone_num_quantity_entry.grid(row=1, column=1, padx=padingx, pady=padingy, sticky=W)

    if is_called_in_custom:
        phone_num_generate_button = Button(build_frame, text="Confirm Selection", command=phone_num_generate_command)
        phone_num_generate_button.grid(row=2, column=1, padx=padingx, pady=padingy)

        phone_num_back = Button(build_frame, text="Change Selection", command=back_out)
        phone_num_back.grid(row=2, column=0, padx=padingx, pady=padingy)

        phone_num_error_label = Label(build_frame, textvariable=phone_error, foreground="red")
        phone_num_error_label.grid(row=3, column=1, padx=padingx, pady=padingy)
    else:
        phone_num_generate_button = Button(build_frame, text="Generate", command=phone_num_generate_command)
        phone_num_generate_button.grid(row=2, column=1, padx=padingx, pady=padingy)

        phone_num_back = Button(build_frame, text="Back", command=return_to_home)
        phone_num_back.grid(row=2, column=0, padx=padingx, pady=padingy)

        phone_num_error_label = Label(build_frame, textvariable=phone_error, foreground="red")
        phone_num_error_label.grid(row=3, column=1, padx=padingx, pady=padingy)
        phone_num_done_label = Label(build_frame, textvariable=phone_done)
        phone_num_done_label.grid(row=4, column=1, padx=padingx, pady=padingy)


create_phone_num_frame(phone_numbers_frame, False)


def create_user_database_frame(build_frame, is_called_in_custom=False):
    global custom_quantity
    global attributes
    global user_database_icon

    def user_database_generate_command():
        user_database_done.set("")
        if is_called_in_custom:
            q = custom_quantity
        else:
            q = user_database_quantity_entry.get()
        file_name = user_database_path.get()
        cus_type = user_database_type.get()
        cd_sort = user_database_sort.get()
        data = []

        if q == "":
            user_database_error.set("Please fill in all options")
            return
        elif file_name == "":
            user_database_error.set("Please fill in all options")
            return
        elif cus_type == "":
            user_database_error.set("Please fill in all options")
            return
        elif cd_sort == "":
            user_database_error.set("Please fill in all options")
            return

        try:
            q = int(q)
            user_database_error.set("")
        except ValueError:
            user_database_error.set("Invalid input for quantity")
            return

        try:
            with open(file_name, 'r') as file:
                csv_reader = csv.reader(file)
                for row in csv_reader:
                    for value in row:
                        data.append(value)
        except PermissionError:
            user_database_error.set(f"Cannot open{file_name}")
        except FileNotFoundError:
            user_database_error.set(f"Cannot find {file_name}")
        except OSError:
            user_database_error.set(f"Error opening {file_name}")

        if cus_type == "Sample":
            if q > len(data):
                user_database_error.set(f"The max sample size for\nthis data set is {len(data)}")
                return

        out = generate_user_database(q, data, cus_type, cd_sort)
        if is_called_in_custom:
            attributes.append(out)
            generate_custom_data()
        else:
            save_path = filedialog.asksaveasfilename(filetypes=accepted_filetypes, defaultextension=accepted_filetypes)
            write_file(out, save_path)
            user_database_done.set("DONE")

    def get_data_file():
        root.filename = filedialog.askopenfilename(filetypes=[('Text Documents', '*.txt'), ('CSV Files', '*.csv')])
        user_database_path.set(root.filename)

    def user_database_help():
        help_info = \
            "User Database allows you to use custom data banks to generate random values.  In order to do this, " \
            "the program requires the database be in CSV format (data is separated by a comma)." \
            "Example: data,data,data,data. The file extension can either be .csv or .txt" \
            "\n\n" \
            "The program also allows you to also specify how data is randomized.\n" \
            "\n- Choices -- The program will randomly choose values from your data. Duplicates are possible.\n" \
            "\n- Sample -- The program will pull a sample set from your data. No duplicates."

        tkinter.messagebox.showinfo("Help", help_info)

    user_database_sort = StringVar()
    user_database_sort.set("")

    user_database_path = StringVar()
    user_database_path.set("")

    user_database_type = StringVar()
    user_database_type.set("")

    user_database_error = StringVar()
    user_database_done = StringVar()

    user_database_intro = Label(build_frame, image=user_database_icon)
    user_database_intro.grid(row=0, column=1, pady=10)

    if is_called_in_custom:
        pass
    else:
        user_database_quantity_label = Label(build_frame, text="Quantity:")
        user_database_quantity_entry = Entry(build_frame)
        user_database_quantity_label.grid(row=1, column=0, padx=padingx, pady=padingy, sticky=E)
        user_database_quantity_entry.grid(row=1, column=1, padx=padingx, pady=padingy, sticky=W)

    user_database_data_label = Label(build_frame, text="Enter Path:")
    user_database_data_label.grid(row=2, column=0, padx=padingx, pady=padingy, sticky=E)

    user_database_data_entry = Entry(build_frame, textvariable=user_database_path)
    user_database_data_entry.grid(row=2, column=1, padx=padingx, pady=padingy, sticky=W)

    user_database_data_button = Button(build_frame, text="Select File", command=get_data_file)
    user_database_data_button.grid(row=2, column=2, padx=padingx, pady=padingy)

    user_database_type_label = Label(build_frame, text="Randomize method:")
    user_database_type_label.grid(row=3, column=0, padx=padingx, pady=padingy, sticky=E)

    user_database_type_select = Combobox(build_frame, textvariable=user_database_type, state='readonly', 
                                         values=('Choices', 'Sample'))

    user_database_type_select.grid(row=3, column=1, padx=padingx, pady=padingy)

    user_database_sort_label = Label(build_frame, text="Sort type:")
    user_database_sort_label.grid(row=4, column=0, padx=padingx, pady=padingy, sticky=E)

    user_database_type_sort_select = Combobox(build_frame, textvariable=user_database_sort, state='readonly',
                                              values=('Ascending', 'Descending', 'No sort'))
    user_database_type_sort_select.grid(row=4, column=1, padx=padingx, pady=padingy)

    if is_called_in_custom:
        user_database_generate_button = Button(build_frame, text="Confirm Selection",
                                               command=user_database_generate_command)
        user_database_generate_button.grid(row=5, column=1, padx=padingx, pady=padingy)

        user_database_back = Button(build_frame, text="Change Selection", command=back_out)
        user_database_back.grid(row=5, column=0, padx=padingx, pady=padingy)

        user_database_error_label = Label(build_frame, textvariable=user_database_error, foreground="red")
        user_database_error_label.grid(row=6, column=1, padx=padingx, pady=padingy)
    else:
        user_database_generate_button = Button(build_frame, text="Generate", command=user_database_generate_command)
        user_database_generate_button.grid(row=5, column=1, padx=padingx, pady=padingy)

        user_database_back = Button(build_frame, text="Back", command=return_to_home)
        user_database_back.grid(row=5, column=0, padx=padingx, pady=padingy)

        user_database_generate_button = Button(build_frame, text="Help", command=user_database_help)
        user_database_generate_button.grid(row=5, column=2, padx=padingx, pady=padingy)

        user_database_error_label = Label(build_frame, textvariable=user_database_error, foreground="red")
        user_database_error_label.grid(row=6, column=1, padx=padingx, pady=padingy)
        user_database_done_label = Label(build_frame, textvariable=user_database_done)
        user_database_done_label.grid(row=7, column=1, padx=padingx, pady=padingy)


create_user_database_frame(user_database_frame, False)


def create_true_false_frame(build_frame, is_called_in_custom=False):
    global custom_quantity
    global attributes
    global true_false_icon

    def true_false_generate_command():
        tf_done.set("")
        if is_called_in_custom:
            q = custom_quantity
        else:
            q = true_false_quantity_entry.get()
        statement = true_false_statement_entry.get()

        if q == "":
            tf_error.set("Please fill in all options")
            return
        elif statement == "":
            tf_error.set("Please fill in all options")
            return

        try:
            q = int(q)
            tf_error.set("")
        except ValueError:
            tf_error.set("Invalid input for quantity")
            return

        out = generate_true_false(q, statement, is_called_in_custom=is_called_in_custom)
        if is_called_in_custom:
            attributes.append(out)
            generate_custom_data()
        else:
            save_path = filedialog.asksaveasfilename(filetypes=accepted_filetypes, defaultextension=accepted_filetypes)
            write_file(out, save_path)
            tf_done.set("DONE")

    tf_error = StringVar()
    tf_done = StringVar()

    true_false_intro = Label(build_frame, image=true_false_icon)
    true_false_intro.grid(row=0, column=1, pady=10)

    if is_called_in_custom:
        pass
    else:
        true_false_quantity_label = Label(build_frame, text="Quantity: ")
        true_false_quantity_entry = Entry(build_frame)
        true_false_quantity_label.grid(row=1, column=0, padx=padingx, pady=padingy, sticky=E)
        true_false_quantity_entry.grid(row=1, column=1, padx=padingx, pady=padingy, sticky=W)

    true_false_statement_label = Label(build_frame, text="Enter a statement:")
    true_false_statement_entry = Entry(build_frame)

    true_false_statement_label.grid(row=2, column=0, padx=padingx, pady=padingy, sticky=E)
    true_false_statement_entry.grid(row=2, column=1, padx=padingx, pady=padingy, sticky=W)

    if is_called_in_custom:
        true_false_generate_button = Button(build_frame, text="Confirm Selection", command=true_false_generate_command)
        true_false_generate_button.grid(row=3, column=1, padx=padingx, pady=padingy)
        true_false_back = Button(build_frame, text="Change Selection", command=back_out)
        true_false_back.grid(row=3, column=0, padx=padingx, pady=padingy)
        true_false_error_label = Label(build_frame, textvariable=tf_error, foreground="red")
        true_false_error_label.grid(row=4, column=1, padx=padingx, pady=padingy)
    else:
        true_false_generate_button = Button(build_frame, text="Generate", command=true_false_generate_command)
        true_false_generate_button.grid(row=3, column=1, padx=padingx, pady=padingy)

        true_false_back = Button(build_frame, text="Back", command=return_to_home)
        true_false_back.grid(row=3, column=0, padx=padingx, pady=padingy)

        true_false_error_label = Label(build_frame, textvariable=tf_error, foreground="red")
        true_false_error_label.grid(row=4, column=1, padx=padingx, pady=padingy)

        true_false_done_label = Label(build_frame, textvariable=tf_done)
        true_false_done_label.grid(row=5, column=1, padx=padingx, pady=padingy)


create_true_false_frame(true_false_frame, False)


def create_card_draws_frame(build_frame, is_called_in_custom=False):
    global custom_quantity
    global attributes
    global card_draws_icon

    def card_draws_generate_command():
        card_done.set("")
        if is_called_in_custom:
            q = custom_quantity
        else:
            q = card_draws_quantity_entry.get()
        nd = card_draws_decks_entry.get()
        sam = card_draws_type_select.get()

        if q == "":
            card_error.set("Please fill in all options")
            return
        elif nd == "":
            card_error.set("Please fill in all options")
            return
        elif sam == "":
            card_error.set("Please fill in all options")
            return

        try:
            q = int(q)
            card_error.set("")
        except ValueError:
            card_error.set("Invalid input for quantity")
            return

        try:
            nd = int(nd)
            card_error.set("")
        except ValueError:
            card_error.set("Invalid input for quantity")
            return
        if sam == "Sample":
            if q > (nd * 52):
                card_error.set("Sample size exceeds\n number of cards")
                return
        out = generate_card_draws(q, nd, sam)
        if is_called_in_custom:
            attributes.append(out)
            generate_custom_data()
        else:
            save_path = filedialog.asksaveasfilename(filetypes=accepted_filetypes, defaultextension=accepted_filetypes)
            write_file(out, save_path)
            card_done.set("DONE")

    def single_draw():
        single_draw_text.set("        Drawing...        ")  # Whitespace there to cover up previous draws
        card_draws_frame.update_idletasks()
        time.sleep(0.8)
        draw = generate_card_draws(1, 1, "Choices")
        single_draw_text.set(draw[0])

    card_error = StringVar()
    card_done = StringVar()

    card_draws_type = StringVar()

    card_draws_intro = Label(build_frame, image=card_draws_icon)
    card_draws_intro.grid(row=0, column=1, pady=10)

    if is_called_in_custom:
        pass
    else:
        card_draws_quantity_label = Label(build_frame, text="Quantity: ")
        card_draws_quantity_entry = Entry(build_frame)
        card_draws_quantity_label.grid(row=1, column=0, padx=padingx, pady=padingy, sticky=E)
        card_draws_quantity_entry.grid(row=1, column=1, padx=padingx, pady=padingy, sticky=W)

    card_draws_decks_label = Label(build_frame, text="Number of Decks: ")
    card_draws_decks_entry = Entry(build_frame)
    card_draws_decks_label.grid(row=2, column=0, padx=padingx, pady=padingy, sticky=E)
    card_draws_decks_entry.grid(row=2, column=1, padx=padingx, pady=padingy, sticky=W)

    card_draws_type_label = Label(build_frame, text="Randomize method:")
    card_draws_type_label.grid(row=3, column=0, padx=padingx, pady=padingy, sticky=E)

    card_draws_type_select = Combobox(build_frame, textvariable=card_draws_type, values=('Sample', 'Choices'),
                                      state='readonly')
    card_draws_type_select.grid(row=3, column=1, padx=padingx, pady=padingy, sticky=E)

    if is_called_in_custom:
        card_draws_generate_button = Button(build_frame, text="Confirm Selection", command=card_draws_generate_command)
        card_draws_generate_button.grid(row=4, column=1, padx=padingx, pady=padingy)
        card_draws_back = Button(build_frame, text="Change Selection", command=back_out)
        card_draws_back.grid(row=4, column=0, padx=padingx, pady=padingy)
        card_draws_error_label = Label(build_frame, textvariable=card_error, foreground="red")
        card_draws_error_label.grid(row=5, column=1, padx=padingx, pady=padingy)
    else:
        card_draws_generate_button = Button(build_frame, text="Generate", command=card_draws_generate_command)
        card_draws_generate_button.grid(row=4, column=1, padx=padingx, pady=padingy)

        card_draws_back = Button(build_frame, text="Back", command=return_to_home)
        card_draws_back.grid(row=4, column=0, padx=padingx, pady=padingy)

        card_draws_error_label = Label(build_frame, textvariable=card_error, foreground="red")
        card_draws_error_label.grid(row=5, column=1, padx=padingx, pady=padingy)

        card_draws_done_label = Label(build_frame, textvariable=card_done)
        card_draws_done_label.grid(row=6, column=1, padx=padingx, pady=padingy)

        single_draw_text = StringVar()
        single_draw_text.set("")

        single_draw_button = Button(build_frame, text="Single Draw", command=single_draw)
        single_draw_button.grid(row=7, column=0)

        single_draw_label = Label(build_frame, textvariable=single_draw_text)
        single_draw_label.grid(row=7, column=1)


create_card_draws_frame(card_draws_frame, False)

"""RANDOM PEOPLE"""


def people_generate_command():
    global people_error
    global people_done
    people_done.set("")
    q = people_quantity_entry.get()
    nam_typ = people_name_type.get()
    addr = include_address.get()
    addr_type = people_address_type.get()
    people_email = include_email.get()
    people_num = include_phone.get()

    if q == "":
        people_error.set("Please fill in all options")
        return
    elif nam_typ == "":
        people_error.set("Please fill in all options")
        return
    elif addr == "":
        people_error.set("Please fill in all options")
        return
    elif addr_type == "":
        if addr == "No":
            pass
        else:
            people_error.set("Please fill in all options")
            return
    elif people_email == "":
        people_error.set("Please fill in all options")
        return
    elif people_num == "":
        people_error.set("Please fill in all options")
        return

    try:
        q = int(q)
        people_error.set("")
    except ValueError:
        people_error.set("Invalid input for quantity")
        return

    save_path = filedialog.asksaveasfilename(filetypes=accepted_filetypes, defaultextension=accepted_filetypes)
    out = generate_random_people(q, nam_typ, addr, addr_type, people_email, people_num)
    write_file(out, save_path)
    people_done.set("DONE")


# noinspection PyUnusedLocal
def people_show_alt_options(*args):
    if include_address.get() == "Yes":
        people_address_type_label.grid(row=3, column=2, sticky=E)
        people_address_type_select.grid(row=3, column=3, padx=10)
    else:
        people_address_type_label.grid_forget()
        people_address_type_select.grid_forget()


people_error = StringVar()
people_done = StringVar()

people_name_type = StringVar()
people_name_type.set("")

include_address = StringVar()
include_address.set("")

people_address_type = StringVar()
people_address_type.set("")

include_email = StringVar()
include_email.set("")

include_phone = StringVar()
include_phone.set("")

people_intro = Label(people_frame, image=people_icon)
people_intro.grid(row=0, column=1, pady=10)

people_quantity_label = Label(people_frame, text="Quantity: ")
people_quantity_entry = Entry(people_frame)

people_quantity_label.grid(row=1, column=0, padx=padingx, pady=padingy, sticky=E)
people_quantity_entry.grid(row=1, column=1, padx=padingx, pady=padingy, sticky=W)

people_name_type_label = Label(people_frame, text="Enter a name type:")
people_name_type_label.grid(row=2, column=0, padx=padingx, pady=padingy, sticky=E)

people_name_type_select = Combobox(people_frame, textvariable=people_name_type, values=('Male names only',
                                                                                        'Female names only',
                                                                                        'Mixed'), state='readonly')
people_name_type_select.grid(row=2, column=1, padx=padingx, pady=padingy)

people_address_label = Label(people_frame, text="Include address:")
people_address_label.grid(row=3, column=0, padx=padingx, pady=padingy, sticky=E)

people_address_select = Combobox(people_frame, textvariable=include_address, state='readonly', values=('Yes', 'No'))
people_address_select.grid(row=3, column=1, padx=padingx, pady=padingy)

people_address_type_label = Label(people_frame, text="Type of address:")
people_address_type_select = Combobox(people_frame, textvariable=people_address_type, state='readonly',
                                      values=('Full address', 'Street address only'))

people_address_select.bind('<<ComboboxSelected>>', people_show_alt_options)

people_email_label = Label(people_frame, text="Include email")
people_email_label.grid(row=4, column=0, padx=padingx, pady=padingy, sticky=E)

people_email_select = Combobox(people_frame, textvariable=include_email, state='readonly', values=('Yes', 'No'))
people_email_select.grid(row=4, column=1, padx=padingx, pady=padingy)

people_number_label = Label(people_frame, text="Include phone number")
people_number_label.grid(row=5, column=0, padx=padingx, pady=padingy, sticky=E)

people_number_select = Combobox(people_frame, textvariable=include_phone, state='readonly', values=('Yes', 'No'))
people_number_select.grid(row=5, column=1, padx=padingx, pady=padingy)

people_generate_button = Button(people_frame, text="Generate", command=people_generate_command)
people_generate_button.grid(row=6, column=1, padx=padingx, pady=padingy)

people_back = Button(people_frame, text="Back", command=return_to_home)
people_back.grid(row=6, column=0, padx=padingx, pady=padingy)

people_error_label = Label(people_frame, textvariable=people_error, foreground="red")
people_error_label.grid(row=7, column=1, padx=padingx, pady=padingy)

people_done_label = Label(people_frame, textvariable=people_done)
people_done_label.grid(row=8, column=1, padx=padingx, pady=padingy)

"""RANDOM STUDENTS"""


def students_generate_command():
    global student_error
    global student_done
    student_done.set("")
    q = students_quantity_entry.get()
    snt = student_name_type.get()
    maj = include_major.get()
    gpa = include_gpa.get()
    c = include_class.get()

    if q == "":
        student_error.set("Please fill in all options")
        return
    elif snt == "":
        student_error.set("Please fill in all options")
        return
    elif maj == "":
        student_error.set("Please fill in all options")
        return
    elif gpa == "":
        student_error.set("Please fill in all options")
        return
    elif c == "":
        student_error.set("Please fill in all options")
        return

    try:
        q = int(q)
        student_error.set("")
    except ValueError:
        student_error.set("Invalid input for quantity")
        return

    save_path = filedialog.asksaveasfilename(filetypes=accepted_filetypes, defaultextension=accepted_filetypes)
    out = generate_random_students(q, snt, maj, gpa, c)
    write_file(out, save_path)
    student_done.set("DONE")


student_error = StringVar()
student_done = StringVar()

student_name_type = StringVar()
student_name_type.set("")

include_major = StringVar()
include_major.set("")

include_gpa = StringVar()
include_gpa.set("")

include_class = StringVar()
include_class.set("")

students_intro = Label(students_frame, image=students_icon)
students_intro.grid(row=0, column=1, pady=10)

students_quantity_label = Label(students_frame, text="Quantity: ")
students_quantity_entry = Entry(students_frame)

students_quantity_label.grid(row=1, column=0, padx=padingx, pady=padingy, sticky=E)
students_quantity_entry.grid(row=1, column=1, padx=padingx, pady=padingy, sticky=W)

students_name_type_label = Label(students_frame, text="Enter a name type:")
students_name_type_label.grid(row=2, column=0, padx=padingx, pady=padingy, sticky=E)

students_name_type_select = Combobox(students_frame, textvariable=student_name_type, values=('Male names only',
                                                                                             'Female names only',
                                                                                             'Mixed'), state='readonly')
students_name_type_select.grid(row=2, column=1, padx=padingx, pady=padingy)

students_address_label = Label(students_frame, text="Include major:")
students_address_label.grid(row=3, column=0, padx=padingx, pady=padingy, sticky=E)

students_address_select = Combobox(students_frame, textvariable=include_major, state='readonly', values=('Yes', 'No'))
students_address_select.grid(row=3, column=1, padx=padingx, pady=padingy)

students_email_label = Label(students_frame, text="Include GPA:")
students_email_label.grid(row=4, column=0, padx=padingx, pady=padingy, sticky=E)

students_email_select = Combobox(students_frame, textvariable=include_gpa, state='readonly', values=('Yes', 'No'))
students_email_select.grid(row=4, column=1, padx=padingx, pady=padingy)

students_number_label = Label(students_frame, text="Include class:")
students_number_label.grid(row=5, column=0, padx=padingx, pady=padingy, sticky=E)

students_number_select = Combobox(students_frame, textvariable=include_class, state='readonly', values=('Yes', 'No'))
students_number_select.grid(row=5, column=1, padx=padingx, pady=padingy)

students_generate_button = Button(students_frame, text="Generate", command=students_generate_command)
students_generate_button.grid(row=6, column=1, padx=padingx, pady=padingy)

students_back = Button(students_frame, text="Back", command=return_to_home)
students_back.grid(row=6, column=0, padx=padingx, pady=padingy)

students_error_label = Label(students_frame, textvariable=student_error, foreground="red")
students_error_label.grid(row=7, column=1, padx=padingx, pady=padingy)

students_done_label = Label(students_frame, textvariable=student_done)
students_done_label.grid(row=8, column=1, padx=padingx, pady=padingy)

"""RANDOM EMPLOYEES"""


def employees_generate_command():
    global employees_error
    global employees_done
    employees_done.set("")
    q = employees_quantity_entry.get()
    ent = employees_name_type.get()
    pos = include_position.get()
    sal = include_salary.get()
    yw = include_years_worked.get()

    if q == "":
        employees_error.set("Please fill in all options")
        return
    elif ent == "":
        employees_error.set("Please fill in all options")
        return
    elif pos == "":
        employees_error.set("Please fill in all options")
        return
    elif sal == "":
        employees_error.set("Please fill in all options")
        return
    elif yw == "":
        employees_error.set("Please fill in all options")
        return

    try:
        q = int(q)
        employees_error.set("")
    except ValueError:
        employees_error.set("Invalid input for quantity")
        return

    save_path = filedialog.asksaveasfilename(filetypes=accepted_filetypes, defaultextension=accepted_filetypes)
    out = generate_random_employees(q, ent, pos, sal, yw)
    write_file(out, save_path)
    employees_done.set("DONE")


employees_error = StringVar()
employees_done = StringVar()

employees_name_type = StringVar()
employees_name_type.set("")

include_position = StringVar()
include_position.set("")

include_salary = StringVar()
include_salary.set("")

include_years_worked = StringVar()
include_years_worked.set("")

employees_intro = Label(employee_frame, image=employees_icon)
employees_intro.grid(row=0, column=1, pady=10)

employees_quantity_label = Label(employee_frame, text="Quantity: ")
employees_quantity_entry = Entry(employee_frame)
employees_quantity_label.grid(row=1, column=0, padx=padingx, pady=padingy, sticky=E)
employees_quantity_entry.grid(row=1, column=1, padx=padingx, pady=padingy, sticky=W)

employees_name_type_label = Label(employee_frame, text="Enter a name type:")
employees_name_type_label.grid(row=2, column=0, padx=padingx, pady=padingy, sticky=E)

employees_name_type_select = Combobox(employee_frame, textvariable=employees_name_type, state='readonly', values=(
                                                                                                    'Male names only',
                                                                                                    'Female names only',
                                                                                                    'Mixed'))

employees_name_type_select.grid(row=2, column=1, padx=padingx, pady=padingy)

employees_address_label = Label(employee_frame, text="Include position:")
employees_address_label.grid(row=3, column=0, padx=padingx, pady=padingy, sticky=E)

employees_address_select = Combobox(employee_frame, textvariable=include_position, state='readonly', values=('Yes',
                                                                                                             'No'))
employees_address_select.grid(row=3, column=1, padx=padingx, pady=padingy)

employees_email_label = Label(employee_frame, text="Include salary:")
employees_email_label.grid(row=4, column=0, padx=padingx, pady=padingy, sticky=E)

employees_email_select = Combobox(employee_frame, textvariable=include_salary, state='readonly', values=('Yes', 'No'))
employees_email_select.grid(row=4, column=1, padx=padingx, pady=padingy)

employees_number_label = Label(employee_frame, text="Include years worked:")
employees_number_label.grid(row=5, column=0, padx=padingx, pady=padingy, sticky=E)

employees_number_select = Combobox(employee_frame, textvariable=include_years_worked, state='readonly', values=('Yes',
                                                                                                                'No'))
employees_number_select.grid(row=5, column=1, padx=padingx, pady=padingy)

employees_generate_button = Button(employee_frame, text="Generate", command=employees_generate_command)
employees_generate_button.grid(row=6, column=1, padx=padingx, pady=padingy)

employees_back = Button(employee_frame, text="Back", command=return_to_home)
employees_back.grid(row=6, column=0, padx=padingx, pady=padingy)

employees_error_label = Label(employee_frame, textvariable=employees_error, foreground="red")
employees_error_label.grid(row=7, column=1, padx=padingx, pady=padingy)

employees_done_label = Label(employee_frame, textvariable=employees_done)
employees_done_label.grid(row=8, column=1, padx=padingx, pady=padingy)

"""CUSTOM FRAME"""

select_1 = StringVar()
select_2 = StringVar()
select_3 = StringVar()
select_4 = StringVar()
select_5 = StringVar()
select_6 = StringVar()

select_1.set("")
select_2.set("")
select_3.set("")
select_4.set("")
select_5.set("")
select_6.set("")

custom_quantity_error = StringVar()
label1_error = StringVar()
label2_error = StringVar()
label3_error = StringVar()
label4_error = StringVar()
label5_error = StringVar()
label6_error = StringVar()


def raise_custom():
    root.geometry('520x500')
    custom_frame.tkraise()


def back_out():
    global custom_quantity
    global attributes
    global labels
    global user_choices
    custom_quantity = 0
    user_choices.clear()
    attributes.clear()
    labels.clear()
    custom_frame.tkraise()


def get_options():
    global labels
    global attributes
    global user_choices
    global custom_quantity
    custom_quantity_error.set("")
    label1_error.set("")
    label2_error.set("")
    label3_error.set("")
    label4_error.set("")
    label5_error.set("")
    label6_error.set("")

    if custom_quantity_entry.get() == "":
        custom_quantity_error.set("Please enter a quantity")
        return
    else:
        custom_quantity = custom_quantity_entry.get()

    try:
        custom_quantity = int(custom_quantity)
        custom_quantity_error.set("")
    except ValueError:
        custom_quantity_error.set("Invalid input for quantity")
        return

    user_choice1 = select_1.get()
    user_choice2 = select_2.get()
    user_choice3 = select_3.get()
    user_choice4 = select_4.get()
    user_choice5 = select_5.get()
    user_choice6 = select_6.get()
    user_label1 = custom_label1_entry.get()
    user_label2 = custom_label2_entry.get()
    user_label3 = custom_label3_entry.get()
    user_label4 = custom_label4_entry.get()
    user_label5 = custom_label5_entry.get()
    user_label6 = custom_label6_entry.get()

    if user_choice1 != "":
        if custom_label1_entry.get() == "":
            label1_error.set("Please enter a label")
            user_choices.clear()
            labels.clear()
            return
        labels.append(user_label1)
        user_choices.append(user_choice1)
    if user_choice2 != "":
        if custom_label2_entry.get() == "":
            label2_error.set("Please enter a label")
            user_choices.clear()
            labels.clear()
            return
        labels.append(user_label2)
        user_choices.append(user_choice2)
    if user_choice3 != "":
        if custom_label3_entry.get() == "":
            label3_error.set("Please enter a label")
            user_choices.clear()
            labels.clear()
            return
        labels.append(user_label3)
        user_choices.append(user_choice3)
    if user_choice4 != "":
        if custom_label4_entry.get() == "":
            label4_error.set("Please enter a label")
            user_choices.clear()
            labels.clear()
            return
        labels.append(user_label4)
        user_choices.append(user_choice4)
    if user_choice5 != "":
        if custom_label5_entry.get() == "":
            label5_error.set("Please enter a label")
            user_choices.clear()
            labels.clear()
            return
        labels.append(user_label5)
        user_choices.append(user_choice5)
    if user_choice6 != "":
        if custom_label6_entry.get() == "":
            label6_error.set("Please enter a label")
            user_choices.clear()
            labels.clear()
            return
        labels.append(user_label6)
        user_choices.append(user_choice6)
    if user_choices:
        generate_custom_data()
    else:
        custom_quantity_error.set("Please fill in at least one option")
        return


custom_intro = Label(custom_frame, image=custom_icon)
custom_intro.grid(row=0, column=1, padx=padingx, pady=padingy)

custom_info = Label(custom_frame, text="Select options below:")
custom_info.grid(row=1, column=1, padx=padingx, pady=padingy, sticky=W)

custom_quantity_label = Label(custom_frame, text="Quantity:")
custom_quantity_label.grid(row=2, column=0, padx=padingx, pady=padingy, sticky=E)

custom_quantity_entry = Entry(custom_frame)
custom_quantity_entry.grid(row=2, column=1, padx=padingx, pady=padingy, sticky=W)

custom_quantity_error_label = Label(custom_frame, textvariable=custom_quantity_error, foreground="red")
custom_quantity_error_label.grid(row=2, column=3, padx=padingx, pady=padingy, sticky=E)

custom_type_select_label = Label(custom_frame, text="Attribute")
custom_type_select_label.grid(row=3, column=1, padx=padingx, pady=padingy, sticky=W)

custom_type_label_label = Label(custom_frame, text="Label")
custom_type_label_label.grid(row=3, column=0, padx=padingx, pady=padingy, sticky=W)

custom_label1_entry = Entry(custom_frame)
custom_label1_entry.grid(row=4, column=0, padx=padingx, pady=padingy, sticky=W)

custom_type_select1 = Combobox(custom_frame, textvariable=select_1, state='readonly', values=('',
                                                                                              'Dates',
                                                                                              'Names',
                                                                                              'Numbers',
                                                                                              'Emails',
                                                                                              'Addresses',
                                                                                              'Phone Numbers',
                                                                                              'User Data',
                                                                                              'True/False',
                                                                                              'Coin Tosses',
                                                                                              'Dice Rolls',
                                                                                              'Card Draws'))

custom_type_select1.grid(row=4, column=1, padx=padingx, pady=padingy, sticky=E)

custom_1_error_label = Label(custom_frame, textvariable=label1_error, foreground="red")
custom_1_error_label.grid(row=4, column=2, padx=padingx, pady=padingy, sticky=E)

custom_label2_entry = Entry(custom_frame)
custom_label2_entry.grid(row=5, column=0, padx=padingx, pady=padingy, sticky=W)

custom_type_select2 = Combobox(custom_frame, textvariable=select_2, state='readonly', values=('',
                                                                                              'Dates',
                                                                                              'Names',
                                                                                              'Numbers',
                                                                                              'Emails',
                                                                                              'Addresses',
                                                                                              'Phone Numbers',
                                                                                              'User Data',
                                                                                              'True/False',
                                                                                              'Coin Tosses',
                                                                                              'Dice Rolls',
                                                                                              'Card Draws'))

custom_type_select2.grid(row=5, column=1, padx=padingx, pady=padingy, sticky=E)

custom_2_error_label = Label(custom_frame, textvariable=label2_error, foreground="red")
custom_2_error_label.grid(row=5, column=2, padx=padingx, pady=padingy, sticky=E)

custom_label3_entry = Entry(custom_frame)
custom_label3_entry.grid(row=6, column=0, padx=padingx, pady=padingy, sticky=W)

custom_type_select3 = Combobox(custom_frame, textvariable=select_3, state='readonly', values=('',
                                                                                              'Dates',
                                                                                              'Names',
                                                                                              'Numbers',
                                                                                              'Emails',
                                                                                              'Addresses',
                                                                                              'Phone Numbers',
                                                                                              'User Data',
                                                                                              'True/False',
                                                                                              'Coin Tosses',
                                                                                              'Dice Rolls',
                                                                                              'Card Draws'))

custom_type_select3.grid(row=6, column=1, padx=padingx, pady=padingy, sticky=E)

custom_3_error_label = Label(custom_frame, textvariable=label3_error, foreground="red")
custom_3_error_label.grid(row=6, column=2, padx=padingx, pady=padingy, sticky=E)

custom_label4_entry = Entry(custom_frame)
custom_label4_entry.grid(row=7, column=0, padx=padingx, pady=padingy, sticky=W)

custom_type_select4 = Combobox(custom_frame, textvariable=select_4, state='readonly', values=('',
                                                                                              'Dates',
                                                                                              'Names',
                                                                                              'Numbers',
                                                                                              'Emails',
                                                                                              'Addresses',
                                                                                              'Phone Numbers',
                                                                                              'User Data',
                                                                                              'True/False',
                                                                                              'Coin Tosses',
                                                                                              'Dice Rolls',
                                                                                              'Card Draws'))

custom_type_select4.grid(row=7, column=1, padx=padingx, pady=padingy, sticky=E)

custom_4_error_label = Label(custom_frame, textvariable=label4_error, foreground="red")
custom_4_error_label.grid(row=7, column=2, padx=padingx, pady=padingy, sticky=E)

custom_label5_entry = Entry(custom_frame)
custom_label5_entry.grid(row=8, column=0, padx=padingx, pady=padingy, sticky=W)

custom_type_select5 = Combobox(custom_frame, textvariable=select_5, state='readonly', values=('',
                                                                                              'Dates',
                                                                                              'Names',
                                                                                              'Numbers',
                                                                                              'Emails',
                                                                                              'Addresses',
                                                                                              'Phone Numbers',
                                                                                              'User Data',
                                                                                              'True/False',
                                                                                              'Coin Tosses',
                                                                                              'Dice Rolls',
                                                                                              'Card Draws'))

custom_type_select5.grid(row=8, column=1, padx=padingx, pady=padingy, sticky=E)

custom_5_error_label = Label(custom_frame, textvariable=label5_error, foreground="red")
custom_5_error_label.grid(row=8, column=2, padx=padingx, pady=padingy, sticky=E)

custom_label6_entry = Entry(custom_frame)
custom_label6_entry.grid(row=9, column=0, padx=padingx, pady=padingy, sticky=W)

custom_type_select6 = Combobox(custom_frame, textvariable=select_6, state='readonly', values=('',
                                                                                              'Dates',
                                                                                              'Names',
                                                                                              'Numbers',
                                                                                              'Emails',
                                                                                              'Addresses',
                                                                                              'Phone Numbers',
                                                                                              'User Data',
                                                                                              'True/False',
                                                                                              'Coin Tosses',
                                                                                              'Dice Rolls',
                                                                                              'Card Draws'))

custom_type_select6.grid(row=9, column=1, padx=padingx, pady=padingy, sticky=E)

custom_6_error_label = Label(custom_frame, textvariable=label6_error, foreground="red")
custom_6_error_label.grid(row=9, column=2, padx=padingx, pady=padingy, sticky=E)

custom_generate = Button(custom_frame, text="Generate", command=get_options)
custom_generate.grid(row=10, column=1, padx=padingx, pady=padingy)

custom_back = Button(custom_frame, text="Back", command=return_to_home)
custom_back.grid(row=10, column=0, padx=padingx, pady=padingy)

"""SELECTIONS FRAME"""

selections_frame.tkraise()
select_label = Label(selections_frame, text="Select a category below:")
select_label.grid(row=0, column=1, columnspan=3, pady=15)

# Row 1

dates_label = Label(selections_frame, text='Dates')
dates_butt = Button(selections_frame, image=dates_icon, command=lambda: dates_frame.tkraise())
dates_butt.grid(row=1, column=0, padx=padingx, pady=padingy)
dates_label.grid(row=2, column=0, padx=padingx, pady=padingy)

numbers_label = Label(selections_frame, text='Numbers')
numbers_butt = Button(selections_frame, image=numbers_icon, command=lambda: numbers_frame.tkraise())
numbers_butt.grid(row=1, column=1, padx=padingx, pady=padingy)
numbers_label.grid(row=2, column=1, padx=padingx, pady=padingy)

names_label = Label(selections_frame, text='Names')
names_butt = Button(selections_frame, image=names_icon, command=lambda: names_frame.tkraise())
names_butt.grid(row=1, column=2, padx=padingx, pady=padingy)
names_label.grid(row=2, column=2, padx=padingx, pady=padingy)

dice_rolls_label = Label(selections_frame, text='Dice Rolls')
dice_rolls_butt = Button(selections_frame, image=dice_rolls_icon, command=lambda: dice_rolls_frame.tkraise())
dice_rolls_butt.grid(row=1, column=3, padx=padingx, pady=padingy)
dice_rolls_label.grid(row=2, column=3, padx=padingx, pady=padingy)

coin_tosses_label = Label(selections_frame, text='Coin Tosses')
coin_tosses_butt = Button(selections_frame, image=coin_tosses_icon, command=lambda: coin_tosses_frame.tkraise())
coin_tosses_butt.grid(row=1, column=4, padx=padingx, pady=padingy)
coin_tosses_label.grid(row=2, column=4, padx=padingx, pady=padingy)

# Row 2

draw_card_label = Label(selections_frame, text='Card Draws')
draw_card_butt = Button(selections_frame, image=card_draws_icon, command=lambda: card_draws_frame.tkraise())
draw_card_butt.grid(row=3, column=0, padx=padingx, pady=padingy)
draw_card_label.grid(row=4, column=0, padx=padingx, pady=padingy)

emails_label = Label(selections_frame, text='Emails')
emails_butt = Button(selections_frame, image=emails_icon, command=lambda: emails_frame.tkraise())
emails_butt.grid(row=3, column=1, padx=padingx, pady=padingy)
emails_label.grid(row=4, column=1, padx=padingx, pady=padingy)

addresses_label = Label(selections_frame, text='Addresses')
addresses_butt = Button(selections_frame, image=addresses_icon, command=lambda: addresses_frame.tkraise())
addresses_butt.grid(row=3, column=2, padx=padingx, pady=padingy)
addresses_label.grid(row=4, column=2, padx=padingx, pady=padingy)

phone_num_label = Label(selections_frame, text='Phone Num')
phone_num_butt = Button(selections_frame, image=phone_num_icon, command=lambda: phone_numbers_frame.tkraise())
phone_num_butt.grid(row=3, column=3, padx=padingx, pady=padingy)
phone_num_label.grid(row=4, column=3, padx=padingx, pady=padingy)

user_database_label = Label(selections_frame, text='User Data')
user_database_butt = Button(selections_frame, image=user_database_icon,
                            command=lambda: user_database_frame.tkraise())
user_database_butt.grid(row=3, column=4, padx=padingx, pady=padingy)
user_database_label.grid(row=4, column=4, padx=padingx, pady=padingy)

# Row 3

true_false_label = Label(selections_frame, text='True/False')
true_false_butt = Button(selections_frame, image=true_false_icon, command=lambda: true_false_frame.tkraise())
true_false_butt.grid(row=5, column=0, padx=padingx, pady=padingy)
true_false_label.grid(row=6, column=0, padx=padingx, pady=padingy)

people_label = Label(selections_frame, text='People')
people_butt = Button(selections_frame, image=people_icon, command=lambda: people_frame.tkraise())
people_butt.grid(row=5, column=1, padx=padingx, pady=padingy)
people_label.grid(row=6, column=1, padx=padingx, pady=padingy)

students_label = Label(selections_frame, text='Students')
students_butt = Button(selections_frame, image=students_icon, command=lambda: students_frame.tkraise())
students_butt.grid(row=5, column=2, padx=padingx, pady=padingy)
students_label.grid(row=6, column=2, padx=padingx, pady=padingy)

employees_label = Label(selections_frame, text='Employees')
employees_butt = Button(selections_frame, image=employees_icon, command=lambda: employee_frame.tkraise())
employees_butt.grid(row=5, column=3, padx=padingx, pady=padingy)
employees_label.grid(row=6, column=3, padx=padingx, pady=padingy)

custom_label = Label(selections_frame, text='Custom')
custom_butt = Button(selections_frame, image=custom_icon, command=raise_custom)
custom_butt.grid(row=5, column=4, padx=padingx, pady=padingy)
custom_label.grid(row=6, column=4, padx=padingx, pady=padingy)

root.mainloop()

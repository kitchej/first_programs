import random
from datetime import datetime

months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November",
          "December"]

s = input("Enter file path. If saving to a new file, enter a new file name at the end of the path:")
r = input("Number of random dates: ")
f = input("Choose date format \na: month day, year; b:  mm/dd/yyyy; c: day month year d: dd/mm/yyyy : ")
print("Specify the range of years. For dates in the same year, make the range start and end the same")
x = input("Range start: ")
y = input("Range end: ")

try:
    for dates in range(int(r)):
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

        date = (str(month) + " " + str(day) + " " + str(year))

        if f == "a":
            try:
                file = open(s, "a+")
                file.write(date + ", ")
                file.close()
            except FileNotFoundError:
                print(FileNotFoundError)
                break
        elif f == "b":
            try:
                d = datetime.strptime(date, "%B %d %Y")
                file = open(s, "a+")
                file.write(d.strftime("%m/%d/%Y") + ", ")
                file.close()
            except FileNotFoundError:
                print(FileNotFoundError)
                break
        elif f == "c":
            try:
                d = datetime.strptime(date, "%B %d %Y")
                file = open(s, "a+")
                file.write(d.strftime("%d %B %Y") + ", ")
                file.close()
            except FileNotFoundError:
                print(FileNotFoundError)
                break
        elif f == "d":
            try:
                d = datetime.strptime(date, "%B %d %Y")
                file = open(s, "a+")
                file.write(d.strftime("%d/%m/%Y") + ", ")
                file.close()
            except FileNotFoundError:
                print(FileNotFoundError)
                break
except ValueError:
    print(ValueError)

print("Done")

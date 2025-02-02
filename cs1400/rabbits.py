"""
Project Name: Project 3 - Rabbit Growth Calculator
Author: Joshua Kitchen
Due Date: 10/17/2020
Course: CS1400-005
"""


def main():
    # Main inputs
    file_name = "rabbits.csv"
    cages = 500
    adults = 1  # This will be the number of starting adults pairs

    # Other inputs
    month = 1
    babies = 0

    # Variables for internal use
    total = adults
    prev_gen_babies = 0

    file = open(file_name, 'a+')
    file.write(
        f"# Table of rabbit pairs\n"
        f"Month, Adults, Babies, Total\n"
        f"{month}, {adults}, {babies}, {total}\n"
    )

    while total <= cages:
        babies = adults * 1
        adults += prev_gen_babies
        total = adults + babies
        prev_gen_babies = babies
        month += 1
        file.write(f"{month}, {adults}, {babies}, {total}\n")

    file.write(f"# Cages will run out in month {month}")
    file.close()


if __name__ == '__main__':
    main()

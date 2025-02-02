"""
Speed Test - v1.0

A simple script to test the speed difference between two algorithms. Outputs results to a csv file and graph the results

"""
import csv
import time
import matplotlib.pyplot as plt

ran = 100  # controls how many numbers start out in the list 'numbers' list
increase = 100  # how many numbers to add to the 'numbers' list each test

loops = 10  # how many times to run the test

# Internal Variables
func1_times = []
func2_times = []
nums = []

# variables for the graph

title = "Title of Plot"
x_axis_lab = "Number of calculations"
y_axis_lab = "Execution Time"

legendLab1 = ("Func1", 'Blue')
legendLab2 = ("Func2", 'Red')


def test_case1(li):  # define algorithm 1 here - li is the list of inputs being passed to algorithm
    pass


def test_case2(li):  # define algorithm 2 here -  li is the list of inputs being passed to algorithm
    pass


for i in range(loops):
    numbers = [n for n in range(ran)]  # fills list with numbers based on 'ran' variable

    # Test case 1

    func1_start = time.perf_counter()
    test_case1(numbers)
    func1_end = time.perf_counter()
    func1_times.append(func1_end - func1_start)

    # Test_case 2

    func2_start = time.perf_counter()
    test_case2(numbers)
    func2_end = time.perf_counter()
    func2_times.append(func2_end - func2_start)

    nums.append(ran)
    ran += increase


with open("Stats.csv", 'w+') as file:
    writer = csv.writer(file)
    writer.writerow(func1_times)
    writer.writerow(func2_times)
    writer.writerow(nums)


with open("stats.csv", 'r') as file:
    reader = csv.reader(file)
    times = []
    i = 0
    for line in reader:
        times.append(line)

func1_times = times[0]
func2_times = times[1]
numbers = times[2]

plt.title(title)
plt.plot(numbers, func1_times, label=legendLab1[0], color=legendLab1[1])
plt.plot(numbers, func2_times, label=legendLab2[0], color=legendLab2[1])
plt.xlabel(x_axis_lab)
plt.ylabel(y_axis_lab)

plt.legend(loc="upper left")

plt.show()

print("Hello, my name is Rob. My job is to determine if the age gap between you and the person you want to date is "
      "acceptable.")
stop = input("Please type \"start\" to begin.")
while stop != "done":
    age1 = float(input("How old are you? "))
    age2 = float(input("How old is the person you want to date? "))
    if age2 <= 17 and age1 >= 21:
        print("The FBI is on their way")
    elif age2 >= (age1 / 2) + 7:
        print("This person is old enough to date")
    elif age2 <= (age1 / 2) + 7:
        print("This person is too young to date")
    stop = input("To input another entry, type \"yes\". If you are finished, type\"done\". ")


print("Thank you for using the dating age calculator!")
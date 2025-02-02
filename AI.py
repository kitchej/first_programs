import random
import math

AI_names = ["Rob", "Alan", "Edith", "Carie", "Lucy", "Sam", "Ed", "Luke", "Cindy", "Martha", "Amber", "Edward", "Toby"]

ice_cream = ["Vanilla", "Chocolate", "Strawberry", "Neapolitan", "Pistachio", "Mint Chocolate Chip", "Rocky Road"]

n = random.choice(AI_names)

user_name = input("Hello, my name is " + n + ". What is your name?")

print("Nice to meet you " + user_name)

number = input("What is your favorite number?")

sqrt_num = math.sqrt(int(number))

AI_num = random.randint(1, 9999)

print("Good choice. By the way, the square root of that number is  " + str(sqrt_num))
print("My favorite number is " + str(AI_num))

user_flavor = input("What us your favorite flavor of ice cream?")

i = random.choice(ice_cream)

print(user_flavor + " is a good flavor. Personally, I like " + i)


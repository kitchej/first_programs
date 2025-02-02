import secrets

temp_password = ""


def generate_numbers():
    return str(secrets.randbelow(9))


def generate_special():
    special_char = ['!', '?', '&', '%', '@', '#', '*', '~', '^']
    return secrets.choice(special_char)


def generate_capital():
    capital_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
                       'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    return secrets.choice(capital_letters)


def generate_lowercase():
    lower_case = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                  'u', 'v', 'w', 'x', 'y', 'z']
    return secrets.choice(lower_case)


funcs = [generate_special, generate_numbers, generate_capital, generate_lowercase]

for _ in range(15):
    while True:
        char = secrets.choice(funcs)()
        if char not in temp_password:
            temp_password = temp_password + char
            break


print(temp_password)

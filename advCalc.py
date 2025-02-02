while True:  
    
    expression = input("Enter an expression: ")
    
    if expression == "exit":
        break

    items = expression.split(" ")
    
    try:
        num1 = int(items[0])
        op = items[1]
        num2 = int(items[2])
    except ValueError:
        print("Invalid Input")
        continue
    
    if op == '+':
        print(num1 + num2)
       
    elif op == '-':
        print(num1 - num2)
    
    elif op == '*':
        print(num1 * num2)
    
    elif op == '/':
        try:
            print(num1 / num2)
        except ZeroDivisionError:
            print("Error - Divided by Zero")
    
    elif op == '%':
        try:
            print(num1 % num2)
        except ZeroDivisionError:
            print("Error - Divided by Zero")
    
    else:
        print(f"Operator \"{op}\" not supported")
    

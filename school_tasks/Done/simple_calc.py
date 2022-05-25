o = "+", "-", "*", "/"
while True:
    first = int(input("Enter 1st number: "))
    operation = input("Enter operation: ")
    if operation == "0":
        print("Good bye :)")
        break
    elif operation not in o:
        print("Enter correct operation!")
        continue
    second = int(input("Enter 2nd number: "))
    if second == 0 and operation == "/":
        print("Can't be divided by 0")
    if operation == "+":
        print(first + second)
    elif operation == "-":
        print(first - second)
    elif operation == "*":
        print(first * second)
    elif operation == "/":
        print(first / second)

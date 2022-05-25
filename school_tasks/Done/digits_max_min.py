a = int(input("Input 1st digit: "))
b = int(input("Input 2nd digit: "))
c = int(input("Input 3rd digit: "))

if b < a > c:
    print("Max", a)
    if b > c:
        print("Min", c)
    else:
        print("Min", b)
elif a < b > c:
    print("Max", b)
    if a > c:
        print("Min", c)
    else:
        print("Min", a)
else:
    print("Max", c)
    if a > b:
        print("Min", b)
    else:
        print("Min", a)

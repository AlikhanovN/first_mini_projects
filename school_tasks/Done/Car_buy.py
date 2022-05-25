a = input("Car name: ")
b = int(input("Milage: "))
c = int(input("Year: "))
d = input("Color: ")
e = input("Side: ")
f = int(input("Owners count: "))
g = int(input("Price: "))

if (a == "Toyota" or a == "Lexus") and c > 2004 and f < 3 and (d == "White" or d == "Grey") and e == "Left":
    if b <= 150000 and g <= 10000:
        print("Buy")
    elif b <= 200000 and g <= 8000:
        print("Buy")
    else:
        print("Don't buy")
else:
    print("Don't buy")

x1 = int(input("X1: "))
y1 = int(input("Y1: "))
x2 = int(input("X2: "))
y2 = int(input("Y2: "))

if (y2 == y1 + 2 or y2 == y1 - 2) and (x2 == x1 + 1 or x2 ==  x1 - 1):
    print("Yes")
elif (x2 == x1 + 2 or x2 == x1 - 2) and (y2 == y1 + 1 or y2 == y1 -1):
    print("Yes")
else:
    print("No")

x1 = int(input("X1: "))
y1 = int(input("Y1: "))
x2 = int(input("X2: "))
y2 = int(input("Y2: "))

if x1 > 0 and y1 > 0 and x2 > 0 and y2 > 0:
    print("Yes") 
elif x1 < 0 and y1 > 0 and x2 < 0 and y2 > 0:
    print("Yes")
elif x1 < 0 and y1 < 0 and x2 < 0 and y2 < 0:
    print("Yes")
elif x1 > 0 and y1 < 0 and x2 > 0 and y2 < 0:
    print("Yes")
else:
    print("No")

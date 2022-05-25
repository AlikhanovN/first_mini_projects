print("1 Task")
a = 2 ** 3
b = 3 ** 2
if a > b:
    print("2**3")
else:
    print("3**2")

print("2 Task")
c = 23
d = 45
e = 14
if c > d and c > e:
    print("1st")
elif d > c and d > e:
    print("2nd")
else:
    print("3rd")

print("3 Task")
a1 = 17391
b1 = 546
c1 = 934
if c1 % 17 > a1 % 17 < b1 % 17:
    print("17391")
elif c1 % 17 > b1 % 17 < c1 % 17:
    print("546")
else:
    print("934")

print("4 Task")
x = 13
if x ** 2 > 172:
    print(x**2)
else:
    (x ** 2) ** 2
    print((x ** 2) ** 2)

print("5 Task")
a2 = 46
if a2 % 2 == 0:
    print("Четное")
elif a2 % 3 == 0:
    print("Делится на 3 без остатка")
elif a2 ** 2 > 1000:
     print("Квадрат больше 1000")

print("6 Task")
a3 = 49
if a3 < 21 or a3 > 57:
    print("Разрешено")
else:
    print("Запрещено")

print("7 Task")
a4 = True
if a4 == True:
    print("Всегда True")

print("8 Task")
a5 = 56
if a5 % 2 == 0:   
    print("Четное")
    if a5 % 4 == 0:
        print("Делится на 4 без остатка")
        if (a5 ** 2) > 1000:
            print("Квадрат больше 1000")

print("9 Task")
a6 = 10 // 6
b6 = 10 / 5
if a6 == b6:
    print("Равны")
else:
    print("Не равны")

print("10 Task")
a7 = -3
if a7 < 0:
    print("Число отрицательное")
else:
    print("Not")

print("11 Task")
a8 = 10
b8 = 5
if a8 > 0 and b8 > 0:
    print("Yes")
else:
    print("No")

print("12 Task")
if a8 > b8:
    print(a8 + 2)
else:
    print(b8 + 2)

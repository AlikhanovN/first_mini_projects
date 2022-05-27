print("Task1")
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
    print("Do you want to continue ?")
    a = input(": ")
    if a == "No":
        break
    else:
        continue

print("Task4")
sequence_0 = (14,10,35,45,'60',70,90,0,105,150,10.0,45.0,'70',0)
sequence_1 = (14,10,35,45,'60',70,90,0,105,150,'70')
sequence_2 = (14,10,35,45,'60',70,90,0,105,150,10.0,45.0,'70',0.0)
sequence_3 = (14,10,35,45,'60',70,90,0,105,150,10.0,45.0,'70')

counter = 0
flag = True
for i in sequence_0:
    if flag == False:
        break
    for j in sequence_0:
        if i == j:
            counter += 1
    if counter > 1:
        print("Последовательность sequence_0 не уникальна.")
        flag = False
        break
    counter = 0
if flag == True:
    print("Последовательность sequence_0 уникальна.")

counter = 0
flag = True
for i in sequence_1:
    if flag == False:
        break
    for j in sequence_1:
        if i == j:
            counter += 1
    if counter > 1:
        print("Последовательность sequence_1 не уникальна.")
        flag = False
        break
    counter = 0
if flag == True:
    print("Последовательность sequence_1 уникальна.")

counter = 0
flag = True
for i in sequence_2:
    if flag == False:
        break
    for j in sequence_2:
        if i == j:
            counter += 1
    if counter > 1:
        print("Последовательность sequence_2 не уникальна.")
        flag = False
        break
    counter = 0
if flag == True:
    print("Последовательность sequence_2 уникальна.")

counter = 0
flag = True
for i in sequence_3:
    if flag == False:
        break
    for j in sequence_3:
        if i == j:
            counter += 1
    if counter > 1:
        print("Последовательность sequence_3 не уникальна.")
        flag = False
        break
    counter = 0
if flag == True:
    print("Последовательность sequence_3 уникальна.")

print("test 5")
flag = True
while flag == True:
    text = input("Decribe reversed funksion: ")
    if text.isdigit() == True:
        print("Try again")
        continue
    a = reversed(list(text))
    for i in a:
        print(i, end="")
    flag = False

#2Aidana
A = int(input('a: '))
B = int(input('b: '))
C = int(input('c: '))
A , B, C = A + B , C - A , A + B + C
print(A , B, C)

#3Aidana
square = int(input('сторона квадрата: '))
p = square*4
s = square**2
print('периметр:', p,'площадь:', s)

#6Aidana
a = input('введите четырехзначное число: ')
c = 0
for i in range(len(a)):
    if a[i] < a[i-1]:
       c += 1
if c == len(a) - 1:
    print(True) 
else:
    print(False)

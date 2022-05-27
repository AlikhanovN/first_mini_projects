'''
Task 1 - Aidana
Task 2 - Aidana
Task 5 - Aidana
'''

print("Task 3")
a = 4729461084
counter = 0
while a:
    counter += a % 10
    a //= 10
print(counter)

print("Task 4")
data = input("Data format (2020-10-24 18:30): ")
time = data.split(" ")[1]
new_data = data.split(" ")[0].split("-")
print(new_data.extend(time))
data_dict = {}
data_dict["year"] = new_data[0]
data_dict["month"] = new_data[1]
data_dict["day"] = new_data[2]
data_dict["time"] = time
print(data_dict)

print("Task6")
print("mkdir -p new/new2")

print("Task7")
print("cd ~alikhanov/Desktop/")

print("Task8")
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for i in a:
    if i > 5:
        print(i)

print("Task9")
digits = (113,118,-5,1,135,137,0,142,144,17,154,0,155,2,159,172)
for i in digits:
    print(i / 9)

print("Task10")
spisok_1 = {'Lamborgini', 17, '4456', 2020, 'Paris', 'USA', 11, 23}
spisok_2 = {'Ferrari', 17, 4456, 2021, 'Paris', 'UK', 777, 23}
print(spisok_2.difference(spisok_1))

print("Task11")
for i in range(301):
    if i % 2 == 0:
        print(i)
    elif i == 237:
        break

print("Task12")
count = 0
text = input("Enter text (min 6 words): ")
for i in text.split(" "):
    count += 1
if count <= 5:
    count = 0
while count <= 5:
    text = input("Enter text (min 6 words): ")
    for i in text.split(" "):
        count += 1
    if count <= 5:
        count = 0
new_t = text[0:(len(text) // 2) + 1]
new_2 = text[(len(text) // 2) + 1::]
new_3 = new_2 + new_t
print(new_t)
print(new_3)

''' Aidana
Task13
Task14
Task15
Task16
'''
#1
print('Task1')
count = 0
for i in range(1, 10):
    if i % 3 ==0 or i % 5 ==0:
        count += i
print(count)
#1.1
count1 = 0
for i in range(1, 1000):
    if i % 3 ==0 or i % 5 ==0:
        count1 += i
print(count1)

#2
print('Task2')
a = 333
b = 555
a , b = b , a
print(a , b)

#5
print('Task5')
a = True
print(a, a*5)
print(a, a*7)

#3
print('Task13')
numbers = [2,4,7,1,8.4,-3.3,7.1,-2,4,-1,7,-43,8,-3,6,9]
num0 = 0
num1 = 0
for i in numbers:
    if type(i) == float:
        i *= 10
    if i % 2 == 0:
        num0 += 1
    elif i % 2 == 1:
        num1 += 1
print('numbers = [2,4,7,1,8.4,-3.3,7.1,-2,4,-1,7,-43,8,-3,6,9]')
print('количество не четных чисел: ' , num1)
print('количество четных чисел: ' , num0)

#4
print('Task14')
numbers2 = [0,2,4,7,1,8,0,-3,7,0,-2,4,0,0,-1,7,-43,0,8,-3,6,9] 
num2 = []
for i in numbers2:
    if i < 0:
        num2.append(-1)
    elif i > 0:
        num2.append(1)
print(num2)

#5
print('Task15')
my_list = [2,4,6,8,10,1,3,5,7,9,11,13,17]
print(my_list)
for i in range(0, len(my_list), 2):
    print(my_list[i])


#6
print('Task16')
numbers = [1,0,-2,4,3,6,6,3,5,8,4,2]
print('numbers = [1,0,-2,4,3,6,6,3,5,8,4,2]')
for i in range(1, len(numbers)):
    if numbers[i] > numbers[i - 1]:
        print(numbers[i])

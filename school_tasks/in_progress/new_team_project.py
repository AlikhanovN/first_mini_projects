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

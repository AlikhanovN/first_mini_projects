print("1 Test")

lang1 = 'Rust'
languages = ['go', 'java', 'php', 'python', 'javascript', 'ruby']
for i in languages:
    if i == lang1:
        print("this languages is in list")

print("2 Test")

for i in languages:
    if i == "php":
        break

print("3 Test")

for i in range(5):
    a = 7 * 7

print("4 Test")

a = 1
for i in languages:
    print(a, i)
    a += 1

a = -1
print("5 Test")
while a:
    if a < 0:
        print(-a, end=",")
    else:
        print(a, end=",")
    a -= 1
    if a == -11:
        a = 9

print("6 Test") 

names = ('Максат','Лязат','Данияр','Айбек','Атай','Салават','Адинай','Жоомарт','Алымбек','Эрмек','Дастан','Бекмамат','Аслан',)
for i in names[::2]:
    print(i, end=",")

print("7 Test")

for i in names[1::2]:
    print(i, end=",")

print("8 Test")

a = 2342
if a > 100 and a % 31 == 0 and a % 2 == 0 and a % 17 == 0 or (a > 150 and a == 13 ** 2):
    print(a)

print("9 Test")

counter1 = 0
counter2 = 0
for i in range(-100, 100):
    if i % 13 == 0 and i % 2 == 0:
        i ** 2
        counter1 +=1
for i in range(-100, 100, 7):
    if i % 2 != 0:
        print(i)
        counter2 += 1
print(counter1, counter2)

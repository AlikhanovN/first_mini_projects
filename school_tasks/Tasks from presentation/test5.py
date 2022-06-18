print("N1")
test = 1, 2, 3, 4, 5

print("N2")
test2 = 1, 2, 3
print(test[0], test[1], test[2])

print("N3")
test3 = [1, "N", 5.5, True, ("a", "b")]

print("N4")
test4 = ["Alex", "Aidana", "Anastasiya", "Kairat", "Elnura"]
a = [" "]
l = []
for i in range(len(test4)):
    l.append(test4[i] + a[0])
print(l)

print("N4")
test9 = ["Alex", "Aidana", "Anastasiya", "Kairat", "Elnura"]
a = " "
a = a.join(test9)
print(a)

print("N5")
test5 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15)
a = 0
for i in range(5):
    print(test5[a], test5[a + 1], test5[a + 2])
    a = a + 3

print("N6")
NAMES = ['JACK', 'JIMMY', 'JACKSON', 'JHON', 'JACKSON', 'JHON',  'JIMMY', 'JACKSON', 'JHON','JACK', 'JIMMY', 'JACK', 
'JACKSON', 'JHON', 'JACKSON', 'JHON','JACK', 'JIMMY', 'JACK', 'JACKSON', 'JHON',]
print(NAMES.count("JACK"))

print("N7")
for i in range(1, 8, 2):
    NAMES.pop(i)
print(NAMES)

print("N8")
test6 = []
a = ["Namik", 1994, "Python"]
test6.extend(a)
print(test6)

import my_module
#task 2
from random import choice, choices
names = ["Aibek", "Joomart", "Adinai", "Ermek", "Atai", "Aslan", "Lyazat", "Salavat", "Daniyar", "Bolotbek", "Alymbek", "Dastan", "Maksat"]
names_l = []
for i in range(4):
    names_l.append(choice(names))
print(names_l)
#task 3
import sys
print(sys.platform)
#task 4
'''
i = input('-> ')
sys.stderr.write(i)
print(sys.argv)
'''
#task 5
"""
import os
try:
    os.mkdir("Name")
except:
    print("file already exist")
for i in range(5):
    a = "qwertyuiopsdfghjklzxcvbnm"
    b = list(a)
    c = ""
    for i in range(4):
        c += choice(b)
    z = open(f"/Users/alikhanov/Documents/Python/Name/{c}", "x")
    z.close()

#task 6
names = ["Aibek", "Joomart", "Adinai", "Ermek", "Atai", "Aslan", "Lyazat", "Salavat", "Daniyar", "Bolotbek", "Alymbek", "Dastan", "Maksat"]
names_1 = []
names_2 = []
names_3 = []
names_4 = []
n_s = set(names)
print(n_s)
c = 0
for i in range(3):
    names_1.append(list(n_s)[i + c])
    names_2.append(list(n_s)[i + 1 + c])
    names_3.append(list(n_s)[i + 2 + c])
    names_4.append(list(n_s)[i + 3 + c])
    c += 3
names_4.append(list(n_s)[-1])
print(names_1)
print(names_2)
print(names_3)
print(names_4)
"""
for a in range(1, 151):
    for b in range(a, 151):
        for c in range(b, 151):
            for d in range(c, 151):
                sum = a ** 5 + b ** 5 + c ** 5 + d ** 5
                e = int(sum ** (1/5))
                if sum == e ** 5:
                    print(a, b, c, d, e)
                    print(a + b + c + d + e)
                    break
John = [["algebra", 100], ["biologia", 84], ["fizika", 61]]
j = dict(John)
a = 0
for i, r in j.items():
    a += r
a = a // len(j)
print(a)

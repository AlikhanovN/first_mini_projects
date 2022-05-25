print("1.\n")
a = "*"
for i in range(1, 6):
    print(a * i)


a = "*"
print("\n2.\n")
for i in range(1, 6):
    print(a * i)
for i in range(4, 0, -1):
    print(a * i)

print("\n3.")
a = "*"
b = " "
c = 0
for i in range(2, 14, 2):
    print(b * (8 - i + c), a)
    a = "*"
    c += 1
    a *= i
a = "*" * 8
b = " "
c = 0
for i in range(6, -2, -2):
    print(b * (8 - i - c), a)
    a = "*"
    a *= i
    c += 1
print(b * 6, '*')

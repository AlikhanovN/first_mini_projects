counter = 0
a = int(input("Enter number: "))
for i in range(len(str(a))):
    b = a % 10
    if b > counter:
        counter = b
    a //= 10
print(counter)

counter = 0
a = int(input("Enter: "))
while a:
    counter += a % 10
    a //= 10
print(counter)

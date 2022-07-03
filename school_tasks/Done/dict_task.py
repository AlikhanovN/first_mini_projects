dict1 = {'a': 5, 'b': 3, 'c': 8, 'd': 14}
for i, j in dict1.items():
    if j % 5 == 0:
        print(i, "Hi")
    elif j % 3 == 0:
        print(i, "Bye")

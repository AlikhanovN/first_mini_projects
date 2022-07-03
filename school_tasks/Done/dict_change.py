a, b, c = 0, 0, 0
d = []
my_dict = {'a': 500, 'b': 5874, 'c': 560, 'd': 400, 'e': 5874, 'f': 20}
for i, j in my_dict.items():
    if j > a:
        c = b
        b = a
        a = j
        d.append(i)
    elif j > b and j != a:
        c = b
        b = j
        d.append(i)
    elif j > c and j != b and j != a:
        c = j
        d.append(i)
for i in d:
    my_dict.pop(i)
print(my_dict)


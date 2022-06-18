def delimeter():
    a = [-1, -2, -3, 5, 6, 7]
    b = []
    c = []
    for i in a:
        if i > 0:
            b.append(i)
        else:
            c.append(i)
    print(b, c)
delimeter()

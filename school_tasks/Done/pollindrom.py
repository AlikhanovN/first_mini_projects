words = ['Anna', 'Civic', 'Kayak', 'Level', 'Madam', 'Mom', 'Noon', 'Racecar', 'Radar', 'еще', 'кабак', 'шалаш', 'лишил','language', 'which', 'means', 'vendor', 'слова', 'фраза', 'введите', 'слово', 'кнопку',]
a, b, c, d = "", "", "" , ""
for i in words:
    if len(i) % 2 != 0:
        a = i[: (len(i) - 1) // 2].lower()
        for j in reversed(i[(len(i) - 1) // 2 + 1:]):
            b += j
        if a == b:
            print(i, "Polindrom")
        a = ""
        b = ""
    else:
        c = i[: len(i) // 2].lower()
        for k in reversed(i[len(i) // 2:]):
            d += k
        if c == d:
            print(i, "Polindrom")
        c = ""
        d = ""
        
        










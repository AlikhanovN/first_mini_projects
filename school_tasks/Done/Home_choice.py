a = input("Регион: ")
b = input("Кирпич или Пескоблок: ")
c = int(input("Сколько сот: "))
d = int(input("Цена: "))

if a == "Чон Арык" or a == "Байтик" or a == "Ортосай":
    if b == "Кирпич" and c < 4 and d < 50000:
        print("Покупай")
    elif b == "Пескоблок" and c < 5 and d > 50000:
        print("Покупай")
    else:
        print("Не покупай")
else:
    print("Не покупай")

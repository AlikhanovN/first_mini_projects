
#    Задание 7:
#     Чтение из файла.
#     Создайте файл с текстом The Zen of Python.
#     Напишите функцию, которая считайте его и возвратит список из слов, которые начинаются на букву “c” или “C”.
#     Подсказка: используйте метод строчных значений, который проверяет, начинается ли слово на переданную букву.
####################################################################
def zen_ofp():
    with open("/Users/alikhanov/Documents/DreamTeam/Zen.txt", "w+") as zen:
        zen.write(f"""Beautiful is better than ugly.
    Explicit is better than implicit.
    Simple is better than complex.
    Complex is better than complicated. 
    Flat is better than nested.
    Sparse is better than dense.
    Readability counts. 
    Special cases aren't special enough to break the rules.
    Although practicality beats purity.
    Errors should never pass silently.
    Unless explicitly silenced.
    In the face of ambiguity, refuse the temptation to guess.
    There should be one-- and preferably only one --obvious way to do it.
    Although that way may not be obvious at first unless you're Dutch.
    Now is better than never.
    Although never is often better than *right* now.
    If the implementation is hard to explain, it's a bad idea.
    If the implementation is easy to explain, it may be a good idea.
    Namespaces are one honking great idea -- let's do more of those!""")
        zen.seek(0)
        for i in list(zen.read().split(" ")):
            if i.lower()[0] == "c":
                print(i)
#   Задание 8:
#     Банкомат
#     Напишите код банкомата, который принимает цифру, выдает деньги с номиналом
#     5000, 2000, 1000, 500, 200, 100, 50, 20, 10, 5, 3, 1.
#     Подсказка: напишите функцию, используйте divmod()
##################################################################
def bankomat():
    x = int(input("-> "))
    d = divmod(x, 5000)[1]
    print(f"5000 -> {divmod(x, 5000)[0]}")
    print(f"2000 -> {divmod(d, 2000)[0]}")
    print(f"1000 -> {divmod(divmod(d, 2000)[1], 1000)[0]}")
    print(f"500 -> {divmod(divmod(divmod(d, 2000)[1], 1000)[1], 500)[0]}")
    print(f"200 -> {divmod(divmod(divmod(divmod(d, 2000)[1], 1000)[1], 500)[1], 200)[0]}")
    print(f"100 -> {divmod(divmod(divmod(divmod(divmod(d, 2000)[1], 1000)[1], 500)[1], 200)[1], 100)[0]}")
    print(f"50 -> {divmod(divmod(divmod(divmod(divmod(divmod(d, 2000)[1], 1000)[1], 500)[1], 200)[1], 100)[1], 50)[0]}")
    print(f"20 -> {divmod(divmod(divmod(divmod(divmod(divmod(divmod(d, 2000)[1], 1000)[1], 500)[1], 200)[1], 100)[1], 50)[1], 20)[0]}")
    print(f"10 -> {divmod(divmod(divmod(divmod(divmod(divmod(divmod(divmod(d, 2000)[1], 1000)[1], 500)[1], 200)[1], 100)[1], 50)[1], 20)[1], 10)[0]}")
    print(f"5 -> {divmod(divmod(divmod(divmod(divmod(divmod(divmod(divmod(divmod(d, 2000)[1], 1000)[1], 500)[1], 200)[1], 100)[1], 50)[1], 20)[1], 10)[1], 5)[0]}")
    print(f"3 -> {divmod(divmod(divmod(divmod(divmod(divmod(divmod(divmod(divmod(divmod(d, 2000)[1], 1000)[1], 500)[1], 200)[1], 100)[1], 50)[1], 20)[1], 10)[1], 5)[1], 3)[0]}")
    print(f"1 -> {divmod(divmod(divmod(divmod(divmod(divmod(divmod(divmod(divmod(divmod(divmod(d, 2000)[1], 1000)[1], 500)[1], 200)[1], 100)[1], 50)[1], 20)[1], 10)[1], 5)[1], 3)[1], 1)[0]}")

# Задание 12:
#     Аналог шифра цезаря ". Программа должна запрашивать элементы
#     списка через пробел. После чего пользователь должен ввести значение
#     для сдвига элементов списка. Значение может быть как положительным,
#     так и отрицательным. Если значение положительное, элементы списка
#     должны сдвигаться вправо, если отрицательное - влево. Результат
#     необходимо вывести на экран:

#     Пример:
#     [1, 2, 3, 4, 5], сдвиг -2
#     [3, 4, 5, 1, 2]
#####################################################################
def cesar_pass():
    pasw = []
    for i in range(5):
        pasw.append(input(f"Password 5 simvols (left {5 - i}): "))
    b = int(input("Shift: "))
    for i in range(abs(b)):
        if b < 0:
            pasw.append(pasw[0])
            pasw.pop(0)
        if b > 0:
            pasw.insert(0, pasw[-1])
            pasw.pop(-1)
    print(pasw)

# Задание 13:
#     Напишите программу, где исходный список содержит положительные и отрицательные числа.
#     Требуется положительные поместить в один список, а отрицательные - в другой.
###################################################################
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

# Задание 14:
#     Написать функцию season, принимающую 1 аргумент — номер месяца (от 1 до 12), и возвращающую время года, которому этот месяц принадлежит (зима, весна, лето или осень).
#####################################################################
def season():
    a = int(input("Number of month 1-12: "))
    if 5 >= a >= 3:
        print("Spring")
    elif 8 >= a >= 6:
        print("Summer")
    elif 11 >= a >= 9:
        print("Autumn")
    elif a > 12 or a < 1:
        print("Wrong Number")
    else:
        print("Winter")

# Задание 15:

#     Пользователь делает вклад в размере a рублей сроком на years лет под 10% годовых (каждый год размер его вклада увеличивается на 10%. Эти деньги прибавляются к сумме вклада, и на них в следующем году тоже будут проценты).
#     Написать функцию bank, принимающая аргументы a и years, и возвращающую сумму, которая будет на счету пользователя.
#####################################################################
def bank():
    money = int(input("Money: "))
    years = int(input("Years: "))
    for i in range(years):
        money += money * 0.1
    print(f"After {years} years you get {money} money")


# Задание 16:
#     Несколько дней подряд метеоролог измеряет температуру воздуха в своём городе. Ваша программа считывает измеренные им значения и выводит среднее значение температуры за время измерений. Чтобы обозначить конец ввода данных, вводится значение, меньшее -300 (реальная температура не может быть ниже -273.15).
#     При проведении вычислений с действительными числами ответ может незначительно отличаться от математически правильного из-за погрешностей округления; это не повлияет на проверку решения.
########################################################################
def temp():
    a = 0
    counter = 0
    while True:
        b = int(input("Temperature: "))
        if b <= -300:
            break
        else:
            a += b
            counter += 1
    try:
        print(round(a / counter, 2))
    except ZeroDivisionError:
        print("Can not devide to 0!")







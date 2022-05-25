cities = []
while True:
    a = int(input("""
1. Добавить новый город
2. Отобразить список городов
3. Заменить город
4. Удалить город
5. Выход

Input number: """))

    if a == 1:
        new_city = input("Новый город: ")
        if new_city.isdigit() == True:
            print("Некорректное название!")
            continue
        elif new_city not in cities:
            cities.append(new_city)
            print("Город добавлен!")
            continue
        else:
            print("Такой город уже есть!", new_city)
            continue
    elif a == 2:
        print("Список городов: ")
        for i in cities:
            print("-", i)
    elif a == 3:
        current_city = input("Текущий город: ")
        changed_city = input("Новый город: ")
        if current_city.isdigit() == True or changed_city.isdigit() == True:
            print("Некорректное название!")
            continue
        if changed_city in cities:
            print("Такой город уже есть!", changed_city)
            continue
        elif current_city not in cities:
            print("Текущий город отсутствует.")
            continue
        else:
            for i in range(len(cities)):
                if cities[i] == current_city:
                    cities[i] = changed_city
            print("Город заменен.")
            continue
    elif a == 4:
        remove_city = input("Введите название города: ")
        if remove_city.isdigit():
            print("Некорректное название!")
            continue
        elif remove_city not in cities:
            print("Текущий город отсутствует.")
            continue
        else:
            cities.remove(remove_city)
            print("Город удален!")
            continue
    elif a == 5:
        print("Good Bye :)")
        break


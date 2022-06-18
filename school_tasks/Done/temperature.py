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
temp()















a = int(input("Input digit: "))
if 0 < a < 10:
    print("Меньше 10")
elif 10 <= a < 100:
    print("Число в промежутке между 10 и 100")
else:
    print("Число больше 100")

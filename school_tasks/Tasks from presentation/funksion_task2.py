#task1
def add(a, b):
    print(a + b)
def substrack(a, b):
    print(a - b)
def multipy(a, b):
    print(a * b)
def divide(a, b):
    print(a / b)
#task2
def len_w(a):
    b = 0
    for i in a:
        b += 1
    print(b)
#task3
def dict(a, **kwargs):
    a.update(kwargs)
    print(a)
dict({"a": 12}, k=4)
#task4
def menu():
    a = input("-> ")
    b = input("-> ")
    with open("/Users/alikhanov/Desktop/menu.txt", "w") as menu_w:
        menu_w.write(f"For eat: {a}\nFor drink: {b}")
#task5
def creator():
    a = input("-> ")
    open(f"/Users/alikhanov/Documents/Python/Name/{a}", "x")
#task6
def one_in():
    print("Я главная функция")
    def second():
        print("Я вложенная функция")
    second()
#task7
def dictr(**a):
    print(tuple(a.keys()), tuple(a.values()))
#task8
def simple(a):
    counter = 0
    for i in range(1, a + 1):
        if a % i == 0:
            counter += 1
    if counter > 2:
        print("Not simple")
    else:
        print("simple")
#task9
def lst(a, b):
    list1 = list(str(a))
    list2 = list(str(b))
    list1.extend(list2)
    print(list1)
#task10
def repiter():
    a = input("-> ")
    for i in range(int(a)):
        print(a)
#task11
def payslip(a, b=5000):
    print(f"{a} - {b}")
#task12
def generator(a):
    z = "asdfghjklwertyuiopzxcvbnm-@#$%^&234567890"
    for i in z[:a]:
        print(i, end=(""))
generator(10)

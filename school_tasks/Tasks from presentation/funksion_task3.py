#   task 1
print((lambda x, y, z: f"Объём бассейна: {x * y * z}")(1, 2, 3))
#   task 2
import datetime
print((lambda x, y: f"Left: {x - y}")(datetime.datetime.now(), datetime.datetime(2022, 1, 1)))
print((lambda x, y: f"Before: {x - y}")(datetime.datetime(2023, 1, 1), datetime.datetime.now()))
#   task 3
def unc(a):
    if a == 0:
        return "ok"
    if a % 2 != 0:
        print(a)
    unc(a - 1)
print(unc(50))
#   task 4
n_set = {1, 2, 3, 4, 5}
def del_s(a):
    print(a)
    if a == set():
        return "ok"
    a.pop()
    del_s(a)
del_s(n_set)

#   task 5
def unicn(f):
    res = set(f())
    print(res)

@unicn
def rand():
    import random
    l = []
    for i in range(100):
        l.append(random.randint(10, 50))
    return(l)

#   task 6
def crypt(f):
    for i in f():
        print(ord(i), end=" ")
    print()


@crypt
def lg():
    login = "Alex"
    return login

@crypt
def ps():
    passw = "Seven"
    return passw

#   task 7
lst = [1745345,98726,439872634,7312,64872,123687126,9312,4124,231,3123,34,3453]
print(list(map(lambda x: x * 1.185, lst)))

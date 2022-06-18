#   task 1
list_1 = ['name', 'age', '1', '19']
def delimiter():
    list_2 = list(reversed(list_1[:len(list_1) // 2]))
    list_3 = list(reversed(list_1[len(list_1) // 2:]))
    list_2.extend(list_3)
    print(list_2)
delimiter()
#   test 2
def fib():
    fibonaci = [1]
    a = 1
    b = 1
    fibonaci.append(a)
    for i in range(8):
        c = a + b
        fibonaci.append(c)
        a, b = b, a + b
    print(fibonaci)
fib()
#   test 3
a = 8
b = 5
def plus():
    c = a + b
    print(c)
def minus():
    d = a - b
    print(d)
def both():
    plus()
    minus()
both()
#   test 4
def name_cr():
    a = input("-> ")
    open(f"/Users/alikhanov/Documents/Python/Name/{a}", "x")
# print(qwe)
#   test 5
def gen_number():
    from random import choice
    a = "0444"
    b = [1, 4, 5, 7, 9, 0]
    for i in range(6):
        a += str(choice(b))
    print(a)
gen_number()

#test 6
def rec(a):
    print(a)
    if a == 101:
        return a
    else:
        rec(a+2)
rec(1)
#test 7
set_1 = {1, 2, 3, 4, 5, 6, 7, 8}
print(set_1)
def rec_2(a):
    while set_1:
        a.pop()
        print(a)
        rec_2(a)
rec_2(set_1)

#test 8
def rec_3(a):
    b = 2
    c = 3
    print(b, c, end=" ")
    a, b = b, b + a
    c = a + b
    rec_3(a + 1)
rec_3(1)
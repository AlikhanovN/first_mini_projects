
print("Test 1")
values = ("Razakov 32", 10, 1005, ["tables", "chairs"], 23.00)
new_list = []
for i in values:
    try:
        vs = set(i)
    except:
        new_list.append(False)
    else:
        new_list.append(True)
print(all(new_list))

print("Test 2")
n_list = []
for i in range(5):
    n_list.append(int(input("Enter value: ")))
n_set = set(n_list)
print(min(n_set))



print("Test 3")
try:
    eval(input("Enter python funksion: "))
except:
    print("No such funksion")
else:
    print("Good")


print("Test 4")
kredit = int(input("Enter value (more than 50.000): "))
if kredit < 50000:
    print("not_enought")
else:
    print(round(kredit * (3.47 / 100), 2))

print("Test 5")
try:
    "123" - 4
except:
    print("Type Error")
try:
    g + 5
except:
    print("NameError")
try:
    l = [1, 2]
    l[3]
except:
    print("IndexError")

print("Test 6")

values = ("Razakov 32", 10, 1005, ["tables", "chairs"], 23.00)


try:
    at = 10
    rin = 15
    wo = 20

    for e in range(-at, at):
        print(wo / e)
    if at > '5':
        print("at" > 5)
except NameError:
    print("Not such a name")
except:
    print("Any error")

print("Test 7")

lst = []
for i in range(10):
    lst.append(i)

a = list(reversed(lst))
sls_obj = slice(0,8)
print(a[sls_obj])


print("Test 8")
try:
    a = (0)
    b = (1,)
    numbers = []
    while b > a:
        numbers += b
        b += 1
    print(numbers)
except TypeError:
    a = (0)
    b = (1)
    numbers = []
    while b > a:
        numbers.append(b)
        a += 1
    print(numbers)

print("Test 9")
try:
    dict_ = {'name': 'john', 'lastname': 'Snow', 12: 'age'}
    for x in dict_.keys():
        x + 'abc'
except TypeError:
    dict_ = {'name': 'john', 'lastname': 'Snow', "12": 'age'}
    for x in dict_.keys():
        print(x + 'abc')







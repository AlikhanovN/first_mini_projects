print("Sets")
print("N1")

dates_of_birth = {3,10,11,13,31,21,1,10,3,5,6,6}
dates_of_birth.remove(6)
print(dates_of_birth)

print("N2")
new_set = set()
a = {1, 2, 3}
b = {4, 5, 6}
c = {7, 8, 9}
new_set.update(a, b, c)
print(new_set)

print("N3")
farm_1 = {"dog", "cat", "mouse", "sheep"}
farm_2 = {"cow", "horse", "donkey", "cat", "dog"}
print(farm_2.difference(farm_1))

print("N4")
new = set()
d = {"Home", "Nature"}
e = {"Clothers", "Telegram"}
new.update(a, b, c, d, e)
print(new)
new.pop()
print(new)

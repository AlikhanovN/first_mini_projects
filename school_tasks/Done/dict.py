dict_one = {'a':1, 'b':2, 'c':3}
dict_two = {'e':0, 't':4, 'z':5}
dict_three = {'g':7, 'h':8, 'i':9}
dict_four = {}
a = (dict_one, dict_two, dict_three)
for i in a:
    dict_four.update(i)
print(dict_four)

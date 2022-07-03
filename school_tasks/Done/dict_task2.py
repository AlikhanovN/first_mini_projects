school = {"1а": 3, "1б": 5, "2б": 7}
school["1а"] = 4
school["1c"] = 2
school.pop("2б")
print(school)
a = 0
for i in school.values():
    a += i
print(a)

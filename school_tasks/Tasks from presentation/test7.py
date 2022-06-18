print("Dictionary")
print("N1")

menu = {
'lagman': 120, 'plov': '120', 'borsh': 100
}
#   menu.update({"drinks": ["Coca-cola", "Fanta", "Sprite"]})
menu["drinks"] = "Coca-cola", "Fanta", "Sprite"
print(menu)

print("N2")
set_methods = {"add", "remove", "clear", "discard", "pop", "update", "intersection", "difference", "intersection_update"}
dictionary_methods = {"clear", "get", "keys", "values", "items", "update"}
print(set_methods.intersection(dictionary_methods))

print("N3")
login = {}
for i in range(3):
    a = input("Enter login: ")
    b = input("Enter password: ")
    login[a] = b
print(login)


print("N4")
professions = {"Depp": "Actor", "Sem": "Developer", "Jony": "Doctor", "Denny": "Singer", "David": "Baker"}
for j, n in professions.items():
        print("Hi", j, ":), your profession", n, "awesome")

print("N5")

answers = set()
for i in range(10):
    a = int(input("Enter number: "))
    answers.add(a)
answers = tuple(answers)
print(answers, type(answers))

print("N6")
menu = {'lagman': 120, 'plov': '120', 'borsh': 100}
menu["besh_barmak"] = 130
menu["lagman"] = 135
menu.pop("borsh")
print(menu)

print("N7")
south_american_countries = ['Argentina', 'Bolivia', 'Brazil', 'Chile', 'Colombia', 'Ecuador', 'Guyana', 'Paraguay', 'Peru', 
'Suriname', 'Suriname', 'Uruguay', 'Venezuela']
south_american_countries = set(south_american_countries)
south_american_countries = list(south_american_countries)
print(type(south_american_countries), south_american_countries)


print("N8")
suitase = []
b = ["Smartphone", "Charger", "Pen", "Notebook", "Keys"]
suitase.extend(b)
suitase = set(suitase)
suitase.pop()
print(suitase)


print("N9")
farm_1 = {"dog", "cat", "mouse", "sheep"}
farm_2 = {"cow", "horse", "donkey", "cat", "dog"}
print(farm_1.intersection(farm_2))
print(farm_1.difference(farm_2))

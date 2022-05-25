a = int(input("Ram: "))
b = input("SSD or HDD: ")
c = int(input("Memory GB: "))
d = int(input("Cost $: "))

if 4 <= a <= 8 and d <= 1000:
    if b == "SSD" and c >= 256:
        print("Бери")
    elif b == "HDD" and c >= 1000:
        print("Не брать")
    else:
        print("Не брать")
else:
    ("Не брать")

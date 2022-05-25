a = input("Program language: ")
b = int(input("Age: "))
c = int(input("Experiance: "))
d = int(input("Salary: "))

if (a == "Java" or a == "Python" or a == "Javascript") and (18 < b < 65) and c > 3 and d < 60000:
    print("You'r hired! :)")
else:
    print("Try again")

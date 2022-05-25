print("Checker")
age = int(input("Enter age: "))
language = input("What language do you speak: ")
examples = "english", "spasnish", "russian", "kyrgyz"
if 0 > age:
    print("Incorrect age")
elif age > 150:
    print("Incorrect age")
elif language not in examples:
    print("Incorrect language")
else:
    print("Checked in")

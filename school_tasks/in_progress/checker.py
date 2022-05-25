print("Checker")
age = int(input("Enter age: "))
photo = input("Add photo: ")
language = input("What language do you speak: ")
examples = "english", "spasnish", "russian", "kyrgyz"
test = ".jpg", ".png"
if 0 > age:
    print("Incorrect age")
elif age > 150:
    print("Incorrect age")
elif language not in examples:
    print("Incorrect language")
elif photo[photo.find(".")::] not in test:
    print("Incorrect photo format")
else:
    print("Checked in")


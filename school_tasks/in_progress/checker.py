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

#codeofAidana
letters = { 'й', 'ц', 'у', 'к', 'е', 'н', 'г', 'ш', 'щ', 'з', 'х', 'ъ', 'ф', 'ы', 'в', 'а', 'п', 'р', 'о', 'л', 'д', 'ж', 'э', 'я', 'ч', 'с', 'м', 'и', 'т', 'ь', 'б', 'ю', 'ё', 'Й', 'Ц', 'У', 'К', 'Е', 'Н', 'Г', 'Ш', 'Щ', 'З', 'Х', 'Ъ', 'Ф', 'Ы', 'В', 'А', 'П', 'Р', 'О', 'Л', 'Д', 'Ж', 'Э', 'Я', 'Ч', 'С', 'М', 'И', 'Т', 'Ь', 'Б', 'Ю'}

name = input('имя: ')
familyname = input('фамилия: ')
passport = input('passport: ')

print(bool(letters.intersection(set(name.lower()))))
print(bool(letters.intersection(set(familyname.lower()))))

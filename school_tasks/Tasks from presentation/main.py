# Task 1
"""
directories = '''
Applications/ Documents/    Library/      Music/        Public/
Desktop/      Downloads/    Movies/       Pictures/     w/
'''
with open("/Users/alikhanov/Desktop/directories.txt", 'w') as f:
    f.write(directories)
# Task 2
login = input("Login: ")
pasw = input("Password: ")
data = f"Login: {login}\nPassword {pasw}"
with open("/Users/alikhanov/Desktop/users.txt", 'a') as t:
    t.write(data)

# Task 3
g = open("/Users/alikhanov/Desktop/directories.txt", "r")
if "w" in g.read():
    print("Да, в тексте есть w")
else:
    print("Нет, в тексте нет w")
close("/Users/alikhanov/Desktop/directories.txt")

# Task 4

t_words = []
a = '''Python is a widely used high-level programming language for general-purpose
programming, created by Guido van Rossum and first released in 1991. An interpreted
language, Python has a design philosophy that emphasizes code readability (notably
using whitespace indentation to delimit code blocks rather than curly brackets or
keywords), and a syntax that allows programmers to express concepts in fewer lines of
code than might be used in languages such as C++ or JavaT.'''
with open("/Users/alikhanov/Desktop/python.txt", "w+") as n:
    n.write(a)
    n.seek(0)
    for i in n.read().split(" "):
        if "t" in i or "T" in i:
            t_words.append(i)
print(t_words)

# Task 5
with open("/Users/alikhanov/Desktop/login.txt", "a+") as dt:
    login = input("Login: ")
    dt.seek(0)
    if login in dt.read():
        print("Логин уже существует")
    dt.write(f"{login}\n")
    while True:
        with open("/Users/alikhanov/Desktop/database.txt", "a+") as ls:
            pasw = input("Password: ")
            pasw2 = input("Re-enter password: ")
            if pasw2 == pasw:
                base = f"Login: {login}\nPassword: {pasw}\n"
                ls.write(base)
                break
            else:
                print("Пароли не совпадают, введите заного")
                continue

# Task 6
with open("/Users/alikhanov/Desktop/login2.txt", "a+") as dt:
    login = input("Login: ")
    dt.seek(0)
    if login in dt.read():
        print("Логин уже существует")
    dt.write(f"{login}\n")
    while True:
        with open("/Users/alikhanov/Desktop/database2.txt", "a+") as ls:
            pasw = input("Password: ")
            pasw2 = input("Re-enter password: ")
            if pasw2 == pasw:
                base = f"Login: {login}\nPassword: {pasw}\n"
                ls.write(base)
                while True:
                    try:
                        foto = input("Enter photo address: ")
                        if open(foto, "rb"):
                            if foto[foto.find("."):] == ".png" or foto[foto.find("."):] == ".jpg":
                                ls.write(f"Photo address: {foto}")
                                break
                            else:
                                print("Укажи правильный файл")
                                continue
                    except:
                        print("Нет такого файла")
                        break
            else:
                print("Пароли не совпадают, введите заного")
                continue
            break
"""
# Task 7










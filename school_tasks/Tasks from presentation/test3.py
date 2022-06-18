print("Task 1")

text = "Google создаст специальную команду для поиска багов в особо важных приложениях.".split(" ")
print(len(text))

print("Task 2")

text2 = "Запуск Ethereum 2.0 состоится 1 декабря. На депозитный контракт внесено более 524 288 ETH".split(" ")
for i in text2:
    print(i, type(i))

print("Task 3")

text3 = "хакеры слили в сеть данные пакистанской энергетической компании k-Electric".title()
print(text3)

print("Task 4")

a = input("Delimeter: ")
text4 = "GitHub"
print(text4.split(a))

print("Task 5")
text5 = "Ботнет IPStorm , в который ранее входили лишь Windows-машины, увеличился до 13 500 зараженных систем".replace("е", "3")
print(text5)

print("Task 6")
text6 = "Google создаст специальную команду для поиска багов в особо важных приложениях.".split("для")
print(text6[0].upper(), text6[1].lower())

print("Task 7")
text7 = True
print(str(text7), type(str(text7)))

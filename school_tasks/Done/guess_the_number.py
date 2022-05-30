text = []
for i in range(1, 101):
    text.append(str(i))
text_set = set(text)
list1 = list(text_set)
guess_num = int(list1[-1])
print("Guess the hidden number")
for i in range(1, 11):
    print("Try number:", i)
    a = int(input("Guess the number: "))
    if a < guess_num:
        print("Try again, enter higher value")
    elif a > guess_num:
        print("Try again, enter lower value")
    elif a == guess_num:
        print("Congrats! You are win")
        break
print(guess_num)






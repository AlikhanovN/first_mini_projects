total = 0
persentage = 10
flag = True
while flag == True:
    for i in range(6):
        a = int(input("Enter depozit (Max 100k) (To Exit press 0): "))
        if a > 100000:
            print("Overlimit")
        elif a == 0:
            flag = False
            break
        else:
            total += a
    if flag == False:
        break
    total = total + total * 0.1
    print("After 6 month:", total)
print(total)

def season():
    a = int(input("Number of month 1-12: "))
    if 5 >= a >= 3:
        print("Spring")
    elif 8 >= a >= 6:
        print("Summer")
    elif 11 >= a >= 9:
        print("Autumn")
    elif a > 12 or a < 1:
        print("Wrong Number")
    else:
        print("Winter")
season()

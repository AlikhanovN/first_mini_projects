def bank():
    money = int(input("Money: "))
    years = int(input("Years: "))
    for i in range(years):
        money += money * 0.1
    print(f"After {years} years you get {money} money")
bank()

def bankomat():
    x = int(input("-> "))
    d = divmod(x, 5000)[1]
    print(f"5000 -> {divmod(x, 5000)[0]}")
    print(f"2000 -> {divmod(d, 2000)[0]}")
    print(f"1000 -> {divmod(divmod(d, 2000)[1], 1000)[0]}")
    print(f"500 -> {divmod(divmod(divmod(d, 2000)[1], 1000)[1], 500)[0]}")
    print(f"200 -> {divmod(divmod(divmod(divmod(d, 2000)[1], 1000)[1], 500)[1], 200)[0]}")
    print(f"100 -> {divmod(divmod(divmod(divmod(divmod(d, 2000)[1], 1000)[1], 500)[1], 200)[1], 100)[0]}")
    print(f"50 -> {divmod(divmod(divmod(divmod(divmod(divmod(d, 2000)[1], 1000)[1], 500)[1], 200)[1], 100)[1], 50)[0]}")
    print(f"20 -> {divmod(divmod(divmod(divmod(divmod(divmod(divmod(d, 2000)[1], 1000)[1], 500)[1], 200)[1], 100)[1], 50)[1], 20)[0]}")
    print(f"10 -> {divmod(divmod(divmod(divmod(divmod(divmod(divmod(divmod(d, 2000)[1], 1000)[1], 500)[1], 200)[1], 100)[1], 50)[1], 20)[1], 10)[0]}")
    print(f"5 -> {divmod(divmod(divmod(divmod(divmod(divmod(divmod(divmod(divmod(d, 2000)[1], 1000)[1], 500)[1], 200)[1], 100)[1], 50)[1], 20)[1], 10)[1], 5)[0]}")
    print(f"3 -> {divmod(divmod(divmod(divmod(divmod(divmod(divmod(divmod(divmod(divmod(d, 2000)[1], 1000)[1], 500)[1], 200)[1], 100)[1], 50)[1], 20)[1], 10)[1], 5)[1], 3)[0]}")
    print(f"1 -> {divmod(divmod(divmod(divmod(divmod(divmod(divmod(divmod(divmod(divmod(divmod(d, 2000)[1], 1000)[1], 500)[1], 200)[1], 100)[1], 50)[1], 20)[1], 10)[1], 5)[1], 3)[1], 1)[0]}")


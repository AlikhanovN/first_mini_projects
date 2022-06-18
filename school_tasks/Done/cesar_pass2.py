def cesar_pass():
    pasw = []
    for i in range(5):
        pasw.append(input(f"Password 5 simvols (left {5 - i}): "))
    b = int(input("Shift: "))
    for i in range(abs(b)):
        if b < 0:
            pasw.append(pasw[0])
            pasw.pop(0)
        if b > 0:
            pasw.insert(0, pasw[-1])
            pasw.pop(-1)
    print(pasw)
cesar_pass()

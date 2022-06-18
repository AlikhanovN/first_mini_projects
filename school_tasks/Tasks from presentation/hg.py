nums = [3, 2, 4]
target = 6
r = []

n = 1
a = int(input())
for i in range(1, a * 2, 2):
    for j in range(i):
        print(n, end="")
        if n == i // 2 + 1:
            t = n - 1
            for i in range(i // 2):
                print(t, end="")
                t -= 1
            break
        n += 1
    n = 1
    print()


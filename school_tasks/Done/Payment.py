k = int(input("Amount of credit: "))
p = float(input("Precentaige: "))
m = int(input("Month: "))
a = k * 0.01 * p * (1 + 0.01 * p ) ** m / ((1 + 0.01 * p) ** m - 1)
print(a)

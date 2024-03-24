N = input()
F = int(input())
plus = "00"

while int(N[:-2] + plus) % F != 0:
    plus = str(int(plus) + 1).zfill(2)

print(plus)
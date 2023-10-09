N = int(input())
total = 1
next_num = 1 

while next_num < N:
    total += 1
    next_num += 6 * (total - 1)

print(total)
def next_non_zero_integer(k):
    while True:
        k += 1
        if '0' not in str(k):
            return k

n = int(input()) 
for _ in range(n):
    k = int(input())
    next_int = next_non_zero_integer(k)
    print(next_int)
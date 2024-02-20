import sys

def padovan(n):
    if n == 1 or n == 2 or n == 3:
        return 1
    elif n == 4 or n == 5:
        return 2
    else:
        p = [1, 1, 1, 2, 2]
        for i in range(5, n):
            p.append(p[i-2] + p[i-3])
        return p[-1]

T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    print(padovan(N))
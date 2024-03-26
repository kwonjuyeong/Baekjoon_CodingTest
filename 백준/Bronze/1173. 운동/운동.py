import sys

N, m, M, T, R = map(int, sys.stdin.readline().split())
X = m
time, total_time = 0, 0

if m + T > M:
    print(-1)
else:
    while total_time < N:
        if X + T <= M:
            X += T
            total_time += 1
            time += 1
        else:
            X -= R
            if X<m:
                X = m
            time += 1

    print(time)
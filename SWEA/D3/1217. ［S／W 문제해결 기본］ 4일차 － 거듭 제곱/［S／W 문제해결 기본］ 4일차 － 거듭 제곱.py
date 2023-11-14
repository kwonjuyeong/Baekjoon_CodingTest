def double_D(n, m):
    if m == 0:
        return 1
    else:
        return n * double_D(n, m - 1)

for _ in range(10):
    test_case = int(input())
    N, M = map(int, input().split())
    print(f'#{test_case} {double_D(N, M)}')
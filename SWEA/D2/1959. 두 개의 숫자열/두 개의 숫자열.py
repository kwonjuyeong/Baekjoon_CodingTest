T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    max_value = 0

    if len(A) > len(B):
        for i in range(len(A) - len(B) + 1):
            total = 0
            for j in range(len(B)):
                total += A[i + j] * B[j]
            if total > max_value:
                max_value = total
    else:
        for i in range(len(B) - len(A) + 1):
            total = 0
            for j in range(len(A)):
                total += B[i + j] * A[j]
            if total > max_value:
                max_value = total

    print(f'#{test_case} {max_value}')
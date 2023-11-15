T = int(input())
for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    answer = list(map(int, input().split()))
    result = []

    for i in range(1, N + 1):
        if i not in answer:
            result.append(str(i))

    print(f'#{test_case} {" ".join(result)}')
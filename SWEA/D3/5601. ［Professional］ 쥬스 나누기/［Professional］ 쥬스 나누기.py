T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    result = ''

    for i in range(1, N + 1):
        result += f'1/{N} '

    print(f'#{test_case} {result}')
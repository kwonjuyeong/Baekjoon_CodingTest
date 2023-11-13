T = int(input())
for test_case in range(1, T + 1):
    L, U, X = map(int, input().split())
    exercise = 0
    
    if X > U:
        exercise = -1
    elif X < L:
        exercise = L - X

    print(f'#{test_case} {exercise}')
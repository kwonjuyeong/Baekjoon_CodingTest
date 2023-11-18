T = int(input())

for test_case in range(1, T + 1):
    case_num = int(input())
    scores = list(map(int, input().split()))

    frequency = [0] * 101  # 각 숫자의 빈도를 저장할 리스트 (0부터 100까지의 숫자)

    for score in scores:
        frequency[score] += 1

    max_frequency = max(frequency)  # 가장 큰 빈도 수 찾기

    # 가장 큰 빈도를 가진 숫자 중 가장 큰 점수 찾기
    mode = 0
    for i in range(len(frequency)):
        if frequency[i] == max_frequency:
            mode = max(mode, i)

    print(f'#{test_case} {mode}')
T = int(input())

yoil = {'MON': 1, 'TUE': 2, 'WED': 3, 'THU': 4, 'FRI': 5, 'SAT': 6, 'SUN': 0}

for test_case in range(1, T + 1):
    S = input()
    days_to_sunday = 7 - yoil[S]
    print(f'#{test_case} {days_to_sunday}')
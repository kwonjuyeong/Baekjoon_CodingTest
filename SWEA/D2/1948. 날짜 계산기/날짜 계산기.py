T = int(input())
month_day = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

for test_case in range(1, T + 1):
    calender = list(map(int, input().split()))
    first_month, first_day, second_month, second_day = calender
    
    days = 0
    for i in range(first_month, second_month):
        days += month_day[i]
    
    days += second_day
    days -= first_day
    
    print(f'#{test_case} {days + 1}')
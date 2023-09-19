hour,minute = map(int, input().split())
cook_time = int(input())

total = hour * 60 + minute + cook_time

new_hour = (total // 60) % 24
new_minute = total % 60

print(new_hour, new_minute)
# 입력 받기
H, M = map(int, input().split())

total_minutes = H * 60 + M

total_minutes -= 45

if total_minutes < 0:
    total_minutes += 24 * 60
H = total_minutes // 60
M = total_minutes % 60

print(H, M)
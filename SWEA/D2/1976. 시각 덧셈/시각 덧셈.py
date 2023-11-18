T = int(input())
for test_case in range(1, T + 1):
	clock = list(map(int, input().split()))
	hour, minuite = clock[0] + clock[2], clock[1] + clock[3]
	if minuite >= 60:
		minuite -= 60
		hour += 1
	if hour >= 12:
		hour -= 12
	print(f'#{test_case} {hour} {minuite}')        
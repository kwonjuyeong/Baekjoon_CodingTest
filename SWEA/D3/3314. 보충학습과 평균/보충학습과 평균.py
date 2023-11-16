T = int(input())
for test_case in range(1, T + 1):
	average = 0
	li = list(map(int, input().split()))
    
	for i in li:
		if i <= 40:
			average += 40
		else:
			average += i
	print(f'#{test_case} {average // len(li)}')
    
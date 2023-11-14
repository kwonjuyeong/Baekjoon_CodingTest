T = int(input())
for test_case in range(1, T + 1):
	n = int(input())
	num = 0
	for i in range(1, n+1):
		if i % 2 == 0:
			num -= i
		else:
			num += i
	print(f'#{test_case} {num}')        
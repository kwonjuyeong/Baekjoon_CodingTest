T = int(input())

for test_case in range(1, T + 1):
	n = int(input())
	people = list(map(int, input().split()))
	avg = int(sum(people) // len(people))
	cnt = 0
	for i in range(len(people)):
		if people[i] <= avg:
			cnt += 1
	print(f'#{test_case} {cnt}')
                   
                   
                   
        
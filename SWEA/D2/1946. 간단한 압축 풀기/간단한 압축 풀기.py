T = int(input())
for test_case in range(1, T + 1):
	print(f'#{test_case}')
	n = int(input())
	max_lengh = 0
	file = ''

	for i in range(n):
		word, lengh = input().split()
		file += word * int(lengh)
		max_lengh += int(lengh)

	
	for i in range(10, max_lengh, 10):
		print(file[i-10:i])
		if max_lengh - i < 10:
			print(file[i:max_lengh])
       
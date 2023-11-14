moem = ['a', 'e', 'i', 'o', 'u']

T = int(input())
for test_case in range(1, T + 1):
	words = input()
	result = ''
	for word in words:
		if word not in moem:
			result += word
	print(f'#{test_case} {result}')
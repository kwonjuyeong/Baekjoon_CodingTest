T = int(input())
for test_case in range(1, T + 1):
	tree = input()
	a, b = 1, 1
	for i in tree:
		if i == "L":
			a, b = a, a+b
		else:
			a, b = a+b, b
	print(f'#{test_case} {a} {b}')            

T = int(input())
for test_case in range(1, T + 1):
	word = input()
	mirror = word[::-1]
	result = ""
	for i in mirror:
		if i == "b":
			result += "d"
		elif i == "d":
			result += "b"
		elif i == "p":
			result += "q"
		else:
			result += "p"
            
            
	print(f'#{test_case} {result}')            
            
T = int(input())
for test_case in range(1, T + 1):
	n = int(input())
	
	if n % 2 == 0:
		winner = "Alice"
	else:
		winner = "Bob"

	print(f'#{test_case} {winner}')
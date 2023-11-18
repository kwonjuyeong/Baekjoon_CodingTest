from collections import deque

T = int(input())
for test_case in range(1, T + 1):
	numbers = list(map(int, input().split()))
	numbers.sort()
	numbers = deque(numbers)
	numbers.popleft()
	numbers.pop()

	print(f'#{test_case} {round(sum(numbers) / len(numbers))}')
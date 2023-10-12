K = int(input())
numbers = []
for _ in range(K):
	num = int(input())
	if num != 0:
		numbers.append(num)
	else:
		numbers.pop()

print(sum(numbers))
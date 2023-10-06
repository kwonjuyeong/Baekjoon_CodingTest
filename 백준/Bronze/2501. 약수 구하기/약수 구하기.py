N, K = map(int, input().split())
numbers = []

for i in range(1, N+1):
    if N % i == 0:
        numbers.append(i)

numbers.sort()

if K <= len(numbers):
    print(numbers[K-1])
else:
    print(0)

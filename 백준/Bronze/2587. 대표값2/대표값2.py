numbers = []

for _ in range(5):
    n = int(input())
    numbers.append(n)

numbers.sort()
average = sum(numbers) // len(numbers)  # 평균 계산

if len(numbers) % 2 == 1:
    mid = numbers[len(numbers) // 2]
else:
    mid = (numbers[len(numbers) // 2 - 1] + numbers[len(numbers) // 2]) // 2

print(average)
print(mid)
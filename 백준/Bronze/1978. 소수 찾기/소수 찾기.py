N = int(input())
numbers = list(map(int, input().split()))

result = 0

for i in range(N):
    if numbers[i] == 1:
        continue
    
    is_prime = True
    for j in range(2, int(numbers[i] ** 0.5) + 1):
        if numbers[i] % j == 0:
            is_prime = False
            break
    
    if is_prime:
        result += 1

print(result)
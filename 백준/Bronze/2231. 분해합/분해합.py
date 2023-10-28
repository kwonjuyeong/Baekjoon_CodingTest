n = int(input())

result = 0

for i in range(n):
    num = i + sum(map(int, str(i)))
    if num == n:
        result = i
        break
        
print(result)
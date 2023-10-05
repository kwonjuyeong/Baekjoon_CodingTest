raw, cols = 0, 0
max_value = 0

for i in range(9):
    values = list(map(int, input().split()))
    for j in range(9):
        if values[j] > max_value:
            max_value = values[j]
            raw = i
            cols = j

print(max_value)
print(raw+1 , cols+1)
            
            
N, M = map(int, input().split())
A = []
B = []

for _ in range(N):
    row = list(map(int, input().split()))
    A.append(row)
#A = [[1 1 1], [2 2 2], [0 1 0]]
    
for _ in range(N):
    row = list(map(int, input().split()))
    B.append(row)
#B = [[3 3 3], [4 4 4], [5 5 100]]
    
result = []

for i in range(N):
    row = []
    for j in range(M):
        sum_value = A[i][j] + B[i][j]
        row.append(sum_value)
    result.append(row)

for row in result:
    print(*row) 
    
    
N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

# 행렬 B 입력
M, K = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(M)]

# 결과 행렬 초기화
result = [[0] * K for _ in range(N)]

# 행렬 곱셉
for i in range(N):
    for j in range(K):
        for l in range(M):
            result[i][j] += A[i][l] * B[l][j]
            
for row in result:
    print(' '.join(map(str, row)))
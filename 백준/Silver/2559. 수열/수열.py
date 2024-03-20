import sys
input = sys.stdin.readline

result =[]

N, K = map(int,input().split())
num_list = list(map(int, input().split()))
result.append(sum(num_list[:K]))

for i in range(N - K):
    result.append(result[i] - num_list[i] + num_list[K+i])
        
print(max(result))
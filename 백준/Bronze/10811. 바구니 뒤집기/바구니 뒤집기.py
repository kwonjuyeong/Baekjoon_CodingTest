N, M = map(int, input().split())
baskets = list(range(1, N + 1))

for i in range(M):
    i, j = map(int, input().split())
    baskets[i - 1:j] = reversed(baskets[i - 1:j])
    
print(' '.join(map(str, baskets)))  
    
    

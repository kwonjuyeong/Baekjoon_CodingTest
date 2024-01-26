def dfs(start):
    if len(stacks)==M:
        print(' '.join(map(str,stacks)))
        return
    
    for i in range(start, N+1):
        stacks.append(i)
        dfs(i)
        stacks.pop()
        
        
N, M = map(int, input().split())
stacks = []

dfs(1) #1부터 시작
def NandM(N, M, current):
    if len(current) == M:
        print(" ".join(map(str, current)))
        return

    for i in range(1, N+1):
        current.append(i)
        NandM(N, M, current)
        current.pop()
        
N, M = map(int, input().split())
current = []
NandM(N, M, current)
import sys
input = sys.stdin.readline

def backtracking(start):
    if len(result) == M:
        print(" ".join(map(str, result)))
        return 
    for i in range(start, N+1):
        if i not in result:
            result.append(i)
            backtracking(i+1)
            result.pop()

N, M = map(int, input().split())
result = []

backtracking(1)
N = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

moves = 0

for i in range(N):
    if a[i] < b[i]: 
        moves += (b[i] - a[i])

print(moves)
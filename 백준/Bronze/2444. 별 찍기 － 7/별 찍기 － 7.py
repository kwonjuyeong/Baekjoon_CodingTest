N = int(input())

for i in range(1, N + 1):
    spaces = ' ' * (N - i) # 4 3 2 1 
    stars = '*' * (2 * i - 1) # 1 3 5 7 9
    print(spaces + stars)

# N+1번째 줄부터 2N-1번째 줄까지 출력
for i in range(N - 1, 0, -1):
    spaces = ' ' * (N - i) # 1 2 3 4
    stars = '*' * (2 * i - 1) #7 5 3 1
    print(spaces + stars)

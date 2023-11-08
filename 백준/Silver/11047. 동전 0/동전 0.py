import sys
input = sys.stdin.readline

N, K = map(int, input().split())

coins = []

for _ in range(N):
    coins.append(int(input()))

cnt = 0
coins.sort(reverse=True)

for coin in coins:
    if K >= coin:
        count = K // coin
        cnt += count
        K -= count * coin

print(cnt)
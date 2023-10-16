N, M = map(int, input().split())

S = set()
result = 0

for _ in range(N):
    word = input()
    S.add(word)

for i in range(M):
    words = input()
    if words in S:
        result += 1

print(result)
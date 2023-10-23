N, M = map(int, input().split())

deudomot = set()
bodomo = set()

for _ in range(N):
    name = input().strip()
    deudomot.add(name)

result = []
for _ in range(M):
    name = input().strip()
    if name in deudomot:
        result.append(name)

result.sort()
print(len(result))
for name in result:
    print(name)
from sys import stdin

N, M = map(int, input().split())

pocketmons = {}
reverse_pocketmons = {}

for i in range(1, N + 1):
    name = stdin.readline().rstrip()
    pocketmons[i] = name
    reverse_pocketmons[name] = i

for _ in range(M):
    pocketmon = stdin.readline().rstrip()
    if pocketmon.isdigit():
        print(pocketmons[int(pocketmon)])
    else:
        print(reverse_pocketmons[pocketmon])
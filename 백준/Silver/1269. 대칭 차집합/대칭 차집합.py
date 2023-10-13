size_A, size_B = map(int, input().split())
A = set(map(int, input().split()))
B = set(map(int, input().split()))

difference = set()
for a in A:
    if a not in B:
        difference.add(a)
for b in B:
    if b not in A:
        difference.add(b)

# 대칭 차집합의 원소 개수를 출력합니다.
result = len(difference)
print(result)
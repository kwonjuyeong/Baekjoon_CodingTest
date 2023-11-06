import sys
from collections import Counter
input = sys.stdin.readline

N = int(input())
numbers = []

for _ in range(N):
	numbers.append(int(input()))

numbers.sort()

#산술평균
print(round(sum(numbers) / len(numbers)))

#중앙값
print(numbers[len(numbers) // 2])

#최빈값 = Counter.. 여기는 몰랐다.
cnt = Counter(numbers).most_common(2)
if len(numbers) > 1:
    if cnt[0][1] == cnt[1][1]:
        print(cnt[1][0])
    else:
        print(cnt[0][0])
else:
    print(cnt[0][0])
    
#범위
print(max(numbers)-min(numbers))
#print(numbers[N - 1] - numbers[0])

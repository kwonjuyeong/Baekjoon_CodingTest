import sys
input = sys.stdin.readline
N, M = map(int, input().split())
cheapP, cheapO = 1000, 1000

for i in range(M):
	package, one= map(int, input().split())
	if cheapP > package:
		cheapP = package
	if cheapO >one:
		cheapO = one

answer = min(N//6*cheapP + N % 6*cheapO, (N//6+1)*cheapP, cheapO*N)


print(answer)
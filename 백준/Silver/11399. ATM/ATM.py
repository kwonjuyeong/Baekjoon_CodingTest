import sys
input = sys.stdin.readline

N = int(input())
p = list(map(int, input().split()))
p.sort()
time = 0
result = 0


for i in p:
	time += i
	result += time


print(result)
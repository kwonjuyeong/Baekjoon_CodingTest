import heapq
import sys

N = int(input())
heap = []
for i in range(N):
	x = int(sys.stdin.readline())
	if x == 0:
		if len(heap) < 1:
			print(0)
		else:
			print(heapq.heappop(heap))
	else:
		heapq.heappush(heap, x)
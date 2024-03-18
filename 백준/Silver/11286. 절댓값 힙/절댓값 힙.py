import sys, heapq

N = int(sys.stdin.readline())
heap_ = []

for _ in range(N):
	x = int(sys.stdin.readline())
	if x:
		heapq.heappush(heap_, (abs(x), x))
	else:
		if heap_:
			print(heapq.heappop(heap_)[1])
		else:
			print(0)
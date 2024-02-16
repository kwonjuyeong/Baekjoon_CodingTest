import heapq
import sys

N = int(input())
heap = []

# 원소 추가하기
for i in range(N):
    x = int(sys.stdin.readline())
    if x == 0:
        if len(heap) < 1:
            print(0)
        else:
            # 최대 힙의 가장 작은 값(음수로 넣은 값)을 출력
            print(-heapq.heappop(heap))
    else:
        # 음수로 넣어서 최대 힙을 구현
        heapq.heappush(heap, -x)
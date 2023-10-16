N = int(input())

xy_list = []

for i in range(N):
	x, y = map(int, input().split())
	xy_list.append([x, y])

xy_list.sort()


for x, y in xy_list:
	print(x, y)
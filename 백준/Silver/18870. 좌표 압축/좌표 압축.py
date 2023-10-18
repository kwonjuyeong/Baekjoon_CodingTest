N = int(input())
x_list = list(map(int, input().split()))

coord_compression = {}
sorted_x_list = sorted(set(x_list))
for i, x in enumerate(sorted_x_list):
    coord_compression[x] = i

for x in x_list:
    print(coord_compression[x], end=' ')
x, y, w, h = map(int, input().split())

distance = min(x, y, h-y, w-x)

print(distance)
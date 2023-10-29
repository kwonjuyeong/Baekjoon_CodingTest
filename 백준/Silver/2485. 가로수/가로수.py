import math

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

N = int(input())
positions = [int(input()) for _ in range(N)]

positions.sort()

interval = positions[1] - positions[0]
for i in range(2, N):
    interval = gcd(interval, positions[i] - positions[i - 1])

additional_trees = 0
for i in range(1, N):
    additional_trees += (positions[i] - positions[i - 1]) // interval - 1

print(additional_trees)
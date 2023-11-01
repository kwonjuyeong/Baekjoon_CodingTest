n = int(input())
min_bags = float('inf')

for bag5 in range((n // 5) + 1):
    for bag3 in range((n // 3) + 1):
        total_weight = (bag5 * 5) + (bag3 * 3)
        if total_weight == n:
            min_bags = min(min_bags, bag5 + bag3)

if min_bags == float('inf'):
    print(-1)
else:
    print(min_bags)
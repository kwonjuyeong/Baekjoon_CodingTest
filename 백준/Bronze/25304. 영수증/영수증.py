total_price = int(input())
total_item = int(input())
division = 0

for i in range(total_item):
    a, b = map(int, input().split())
    division += a*b
    
if total_price == division:
    print("Yes")
else:
    print("No")
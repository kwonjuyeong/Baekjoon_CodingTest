import sys

N = int(sys.stdin.readline().strip())
new_num = N
cycle = 0

while True:
    if new_num < 10:
        new_num = new_num * 10 + new_num
    else:
        new_num = (new_num % 10) * 10 + ((new_num // 10 + new_num % 10) % 10)
    
    cycle += 1
    
    if new_num == N:
        break

print(cycle)
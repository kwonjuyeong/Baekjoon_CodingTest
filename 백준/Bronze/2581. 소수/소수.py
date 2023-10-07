M = int(input())
N = int(input())

num_list = []

for num in range(M, N+1):
    if num < 2:
        continue
    convert = True    
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            convert = False
            break
    if convert:
        num_list.append(num)
        
if num_list:
    print(sum(num_list))
    print(min(num_list))
else:
    print(-1)
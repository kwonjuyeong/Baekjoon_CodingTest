N = int(input())

sort_list = []

for _ in range(N):
    number = int(input())
    sort_list.append(number)

    
sort_list.sort()

for i in range(len(sort_list)):
    print(sort_list[i])
    
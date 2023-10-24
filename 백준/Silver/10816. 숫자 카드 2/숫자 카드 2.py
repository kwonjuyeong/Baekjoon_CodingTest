N = int(input())
have_list = list(map(int, input().split()))
M = int(input())
find_list = list(map(int, input().split()))

have_dict = {}

for num in have_list:
    if num in have_dict:
        have_dict[num] += 1
    else:
        have_dict[num] = 1

result = []
for num in find_list:
    if num in have_dict:
        result.append(have_dict[num])
    else:
        result.append(0)

print(" ".join(map(str, result)))
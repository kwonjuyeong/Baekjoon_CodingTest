N = int(input())
have_set = set(map(int, input().split()))

M = int(input())
division_list = list(map(int, input().split()))

correct_list = []

for num in division_list:
    if num in have_set:
        correct_list.append("1")
    else:
        correct_list.append("0")

print(" ".join(correct_list))
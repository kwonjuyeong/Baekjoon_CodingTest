a_list = []
b_list = []

for _ in range(3):
    a, b = map(int, input().split())
    a_list.append(a)
    b_list.append(b)

result_a = None
result_b = None

for a in a_list:
    if a_list.count(a) == 1:
        result_a = a

for b in b_list:
    if b_list.count(b) == 1:
        result_b = b

print(result_a, result_b)
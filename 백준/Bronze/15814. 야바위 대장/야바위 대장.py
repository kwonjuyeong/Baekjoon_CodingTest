def swap_characters(s, a, b):
    s_list = list(s)
    s_list[a], s_list[b] = s_list[b], s_list[a]
    result = ''.join(s_list)
    return result

s = input()
t = int(input())

for _ in range(t):
    a, b = map(int, input().split())
    s = swap_characters(s, a, b)

print(s)
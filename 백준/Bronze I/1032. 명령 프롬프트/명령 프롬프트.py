N = int(input())
files = [input() for _ in range(N)]

pattern = ''
for i in range(len(files[0])):
    same_char = True
    for j in range(1, N):
        if files[j][i] != files[0][i]:
            same_char = False
            break
    if same_char:
        pattern += files[0][i]
    else:
        pattern += '?'

print(pattern)
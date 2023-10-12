T = int(input())

for _ in range(T):
    stack = []
    vps = input()
    for word in vps:
        if word == '(':
            stack.append(word)
        elif word == ')':
            if stack:
                stack.pop()
            else:
                print("NO")
                break
    else:
        if not stack:
            print('YES')
        else:
            print('NO')
import sys

N = int(sys.stdin.readline())
stack = []

for _ in range(N):
    command = sys.stdin.readline().split()
    
    first_part = command[0]
    
    if first_part == "1":
        stack.append(command[1])
    elif first_part == "2":
        if len(stack) > 0:
            print(stack.pop())
        else:
            print("-1")
    elif first_part == "3":
        print(len(stack))
    elif first_part == "4":
        if len(stack) > 0:
            print("0")
        else:
            print("1")
    else:
        if len(stack) > 0:
            print(stack[-1])
        else:
            print("-1")
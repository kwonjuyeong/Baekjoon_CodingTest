from collections import deque
import sys

N = int(sys.stdin.readline())
command_list = deque()

for _ in range(N):
    command = sys.stdin.readline().split()
    first = command[0]

    if first == "push":
        x = int(command[1])
        command_list.append(x)
    elif first == "pop":
        if command_list:
            print(command_list.popleft())
        else:
            print(-1)
    elif first == "size":
        print(len(command_list))
    elif first == "empty":
        if command_list:
            print(0)
        else:
            print(1)
    elif first == "front":
        if command_list:
            print(command_list[0])
        else:
            print(-1)
    elif first == "back":
        if command_list:
            print(command_list[-1])
        else:
            print(-1)
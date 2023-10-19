from collections import deque
N = int(input())
students = deque(map(int, input().split()))
stack = []
target = 1

while students:
    if students[0] == target:
        students.popleft()
        target += 1
    else:
        stack.append(students.popleft())
    while stack:
        if stack[-1] == target:
            stack.pop()
            target+=1
        else:
            break
if not stack:
    print("Nice")
else:
    print("Sad")
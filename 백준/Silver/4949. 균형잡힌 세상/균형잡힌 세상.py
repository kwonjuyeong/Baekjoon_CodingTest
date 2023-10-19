import sys

while True:
    sentence = sys.stdin.readline().rstrip()  # 앞뒤 공백을 제거하지 않고 입력을 읽습니다.

    if sentence == ".":
        break

    stack = []

    balanced = True  # 균형을 이루고 있다고 가정합니다.

    for char in sentence:
        if char in "([":  # 왼쪽 괄호일 때 스택에 추가
            stack.append(char)
        elif char in ")]":  # 오른쪽 괄호일 때 스택 검사
            if not stack:  # 스택이 비어있으면 균형이 안맞는 것
                balanced = False
                break
            top = stack.pop()  # 스택에서 맨 위의 괄호를 꺼냅니다.
            if (char == ")" and top != "(") or (char == "]" and top != "["):
                balanced = False  # 괄호가 서로 짝이 안맞는 경우
                break

    if balanced and not stack:  # 스택이 비어있고 모든 괄호가 짝을 이룬 경우
        print("yes")
    else:
        print("no")
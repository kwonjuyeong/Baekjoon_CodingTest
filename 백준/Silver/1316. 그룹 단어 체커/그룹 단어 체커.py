N = int(input())  # 단어의 개수 N 입력 받기
count = 0  # 그룹 단어의 개수 초기화

for _ in range(N):
    word = input()  # 단어 입력 받기
    is_group_word = True  # 그룹 단어 여부를 판별하기 위한 변수 초기화
    seen = set()  # 이미 나타난 문자를 저장하기 위한 집합 초기화
    prev_char = None  # 이전 문자를 저장하기 위한 변수 초기화

    for char in word:
        if char != prev_char:  # 현재 문자와 이전 문자가 다를 경우
            if char in seen:  # 현재 문자가 이미 나타난 적이 있다면
                is_group_word = False  # 그룹 단어가 아님
                break
            seen.add(char)  # 현재 문자를 집합에 추가
        prev_char = char  # 이전 문자를 현재 문자로 업데이트

    if is_group_word:
        count += 1

print(count)
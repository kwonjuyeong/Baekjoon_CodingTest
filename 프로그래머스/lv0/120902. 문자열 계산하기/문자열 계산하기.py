def solution(my_string):
    try:
        # 문자열을 공백을 기준으로 나눠서 리스트에 저장합니다.
        tokens = my_string.split()
        # 초기값은 첫 번째 숫자로 설정합니다.
        result = int(tokens[0])

        # 순서대로 연산자와 숫자를 확인하면서 계산합니다.
        for i in range(1, len(tokens), 2):
            operator = tokens[i]
            operand = int(tokens[i + 1])

            if operator == '+':
                result += operand
            elif operator == '-':
                result -= operand

        return result
    except Exception as e:
        print("에러 발생:", e)
        return None
def solution(my_string, num1, num2):
    char1 = my_string[num1]
    char2 = my_string[num2]
    
    answer = list(my_string)
    answer[num1] = char2
    answer[num2] = char1
    
    # 리스트를 다시 문자열로 변환
    result = ''.join(answer)
    
    return result
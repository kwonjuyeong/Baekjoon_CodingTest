def solution(s):
    answer = 0
    number = 0
    result_list = s.split()
    
    for i in result_list:
        if i == 'Z':
            answer = answer-int(num)
            num = 0
        else:
            answer += int(i)
            num = i
    
    
    return answer
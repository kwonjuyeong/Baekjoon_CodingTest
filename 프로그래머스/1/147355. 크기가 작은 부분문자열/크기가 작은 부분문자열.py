def solution(t, p):
    numbers = []
    answer = 0
    
    for i in range(len(t)):
        if len(t[i:i+len(p)]) == len(p):
            numbers.append(t[i:i+len(p)])
    
    for i in range(len(numbers)):
        if int(numbers[i]) <= int(p):
            answer += 1
    
    return answer
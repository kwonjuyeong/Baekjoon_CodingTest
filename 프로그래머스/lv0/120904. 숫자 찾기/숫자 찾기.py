def solution(num, k):
    answer = str(num)
    
    for i in range(len(answer)):
        if answer[i] == str(k):
            return i + 1
    return -1    
    
    
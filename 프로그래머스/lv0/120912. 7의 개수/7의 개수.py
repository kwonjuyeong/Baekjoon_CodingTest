def solution(array):
    answer = 0
    num_s = ''
    for i in array:
        num_s += str(i)
        
    answer = num_s.count("7")    
    
    return answer
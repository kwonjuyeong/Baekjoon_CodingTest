def solution(a, b):
    answer = 0
    
    a, b = str(a), str(b)
    
    return int(max(a+b, b+a))
    
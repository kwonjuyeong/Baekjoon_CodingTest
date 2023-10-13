def solution(n):
    answer = ''
    
    while n > 0:
        other = n % 3
        n = n // 3
        answer += str(other)
    
    return int(answer,3)
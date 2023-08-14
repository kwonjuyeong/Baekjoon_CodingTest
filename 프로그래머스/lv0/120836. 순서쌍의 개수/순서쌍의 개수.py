def solution(n):
    answer = 0
    
    for i in range(1, n+1):
        if (i * int(n/i)) == n:
            answer += 1
                
    return answer
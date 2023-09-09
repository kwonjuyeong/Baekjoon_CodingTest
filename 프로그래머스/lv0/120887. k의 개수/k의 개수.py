def solution(i, j, k):
    answer = 0
    
    for num in range(i, j+1):
        for word in str(num):
            if word == str(k):
                answer += 1
    
    return answer
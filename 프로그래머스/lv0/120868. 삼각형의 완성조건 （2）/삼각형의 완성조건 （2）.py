def solution(sides):
    answer = 0
    a, b = sides
    
    #a가 가장 길 떄
    for i in range(a):
        if a < b + i:
            answer += 1
    
    #b가 가장 길 떄
    for i in range(b):
        if b < a + i:
            answer += 1
            
    if a == b:
        answer += 1
    
    return answer
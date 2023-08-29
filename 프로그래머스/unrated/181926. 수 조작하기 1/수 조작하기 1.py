def solution(n, control):
    answer = n
    
    for word in control:
        if word == "w":
            answer += 1
        elif word == "s":
            answer -= 1
        elif word == "d":
            answer += 10
        else:
            answer -= 10
    
    return answer
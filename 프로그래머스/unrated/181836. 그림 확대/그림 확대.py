def solution(picture, k):
    answer = []
    
    for line in picture:
        new_line = ''.join([char * k for char in line])
        answer.extend([new_line] * k)
        
    return answer                  
                
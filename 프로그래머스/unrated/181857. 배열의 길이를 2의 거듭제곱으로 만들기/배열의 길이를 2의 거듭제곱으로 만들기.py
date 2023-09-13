def solution(arr):
    answer = arr
    
    while len(answer) & (len(answer) - 1) != 0:
        answer.append(0)

    return answer
def solution(array):
    answer = []
    maxV = max(array)

    answer.append(maxV)
    
    for i in range(len(array)):
        if array[i] == maxV:
            answer.append(i)
    
    return answer
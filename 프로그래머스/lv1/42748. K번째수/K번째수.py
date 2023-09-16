def solution(array, commands):
    answer = []
    
    for command in commands:
        i, j, k = command
    
        convert = array[i-1:j]
        convert.sort()
        answer.append(convert[k-1])
    
    return answer
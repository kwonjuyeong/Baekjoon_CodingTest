def solution(array, commands):
    answer = []
    
    for m in range(len(commands)):
        i, j, k = commands[m]
        convert = array[i-1:j]
        convert.sort()
        answer.append(convert[k-1])
    
    return answer
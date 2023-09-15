def solution(arr):
    answer = []
    indexes = []
    
    for i in range(len(arr)):
        if arr[i] == 2:
            indexes.append(i)
    
    if len(indexes) == 0:
        answer.append(-1)
    else:
        answer = arr[min(indexes):max(indexes)+1]
    
    return answer
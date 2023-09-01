def solution(arr, n):
    answer = arr
    
    if len(arr) % 2 == 1:
        for i in range(len(arr)):
            if i % 2 == 0:
                answer[i] = answer[i] + n
    else:
        for i in range(len(arr)):
            if i % 2 == 1:
                answer[i] = answer[i] + n
    
    return answer
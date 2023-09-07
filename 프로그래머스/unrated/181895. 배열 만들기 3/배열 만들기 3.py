def solution(arr, intervals):
    answer = []
    
    first, second = intervals
    
    return arr[first[0]:first[1]+1] + arr[second[0]:second[1]+1]
    
    return answer
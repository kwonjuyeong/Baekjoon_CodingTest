def solution(arr):
    answer = arr
    mini = min(arr)
    if len(arr) >1:
        answer.remove(mini)
        return answer
    else :
        return[-1]
def solution(k, score):
    answer = []
    result = []
    for i in score:
        if len(result) < k:
            result.append(i)
        else :
            if i > min(result):
                result.remove(min(result))
                result.append(i)
        result.sort()
        answer.append(result[0])
    return answer
def solution(name, yearning, photo):
    answer = []
    point = {}
    for i in range(len(name)):
        point[name[i]] = yearning[i]
    
    for i in photo:
        score = 0
        for j in i:
            score += point.get(j, 0)
        answer.append(score)
    return answer
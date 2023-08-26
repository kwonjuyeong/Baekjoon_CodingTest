def solution(myString):
    answer = []
    division = myString.split("x")
    
    for i in range(len(division)):
        answer.append(len(division[i]))

    return answer
    
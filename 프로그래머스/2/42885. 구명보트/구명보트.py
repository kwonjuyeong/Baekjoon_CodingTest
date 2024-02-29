def solution(people, limit):
    answer = 0
    people.sort()
    thin, fat = 0, len(people) -1
    
    while(thin <= fat):
        if people[fat] + people[thin] <= limit:
            thin += 1
            fat -= 1
        else:
            fat -= 1
        answer += 1    
    return answer

# 1. 구명보트는 한번에 최대 2명씩 탑승 = 조건
# 2. 무게 제한 -> limit = 조건
# 3. 구명보트를 최대한 적게 사용
def solution(s):
    answer = []
    last_seen = dict()
    
    for i in range(len(s)):
        if s[i] not in last_seen:
            answer.append(-1)
        else:
            answer.append(i-last_seen[s[i]])
        last_seen[s[i]] = i
        
    return answer
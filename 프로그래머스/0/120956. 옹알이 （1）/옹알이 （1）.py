def solution(babbling):
    answer = 0
    zoca = ["aya", "ye", "woo", "ma"]
    
    for i in range(len(babbling)):
        cnt = 0
        keyword = ""
        for j in babbling[i]:
            keyword += j
            if keyword in zoca:
                keyword = ""
                cnt += 1
        if len(keyword) == 0 and cnt != 0:
            answer += 1
    
    return answer
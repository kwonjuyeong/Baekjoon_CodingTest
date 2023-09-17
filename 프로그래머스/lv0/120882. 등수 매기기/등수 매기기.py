def solution(scores):
    n = len(scores)
    rank = [1] * n  # 모든 학생을 1등으로 초기화
    
    for i in range(n):
        for j in range(n):
            if i != j:
                # 현재 학생보다 다른 학생의 평균 점수가 더 높으면 등수를 1 증가시킴
                if sum(scores[i]) < sum(scores[j]):
                    rank[i] += 1
    
    return rank
    
    
    
    
    
    
    
    #answer = []
    
    #for eng, math in scores:
    #    average = (eng + math) / 2
    #    answer.append(average)
        
    #비교하는 부분 추가
    #return answer
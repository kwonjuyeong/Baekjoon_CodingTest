from collections import Counter

def solution(k, tangerine):
    answer = 0
    counts = 0
    
    element_count = Counter(tangerine)
    sorted_elements = sorted(element_count.items(), key=lambda x: x[1], reverse=True)

    for element, count in sorted_elements:
        if counts >= k:
            break
        else:
            counts += count
            answer += 1
            
    return answer



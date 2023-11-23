def solution(common):
    first, second, third = common[:3]
    
    if second - first == third - second: #등차 수열일 경우
        result = common[-1] + (second-first)
    elif second // first == third // second: #등비 수열일 경우
        result = common[-1] * (second//first)  
    return result
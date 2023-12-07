from math import gcd

def solution(numer1, denom1, numer2, denom2):
    answer = []
    
    result_numer = numer1 * denom2 + numer2 * denom1
    result_denom = denom1 * denom2
        
    gcd_num = gcd(result_numer, result_denom)
    
    # 분자와 분모를 최대 공약수로 나누어 줍니다.
    result_numer //= gcd_num
    result_denom //= gcd_num
    
    answer = [result_numer, result_denom]

    
    return answer
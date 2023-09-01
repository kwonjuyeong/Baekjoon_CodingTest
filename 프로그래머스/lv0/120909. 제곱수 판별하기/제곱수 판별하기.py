def solution(n):
    if n < 0:
        return 2

    sqrt = int(n ** 0.5)
    if sqrt * sqrt == n:
        return 1
    else:
        return 2
    
    
#import math
#math.isqrt(n) = math 모듈 제곱근 구하는 함수
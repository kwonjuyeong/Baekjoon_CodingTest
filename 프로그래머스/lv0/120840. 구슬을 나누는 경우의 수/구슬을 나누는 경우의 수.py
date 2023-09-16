def solution(balls, share):
    answer = 0
    n, m, nm = 1, 1, 1
    
    for ball in range(balls):
        n *= ball + 1
    
    for shareC in range(share):
        m *= shareC + 1
    
    for allthing in range(balls - share):
        nm *= allthing +1
    
    
    return n / (nm * m)
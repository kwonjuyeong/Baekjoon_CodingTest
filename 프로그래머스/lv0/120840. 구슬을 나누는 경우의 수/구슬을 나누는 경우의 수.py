def solution(balls, share):
    answer = 0
    balls_parent = 1
    share_child = 1
    ballshare_child = 1
    
    for ball in range(balls):
        balls_parent *= ball + 1
    
    for shareC in range(share):
        share_child *= shareC + 1
    
    for allthing in range(balls - share):
        ballshare_child *= allthing +1
    
    
    return balls_parent / (ballshare_child * share_child)
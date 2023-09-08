def solution(n):
    composite_count = 0
    
    for i in range(2, n + 1):
        divisors_count = 0
        
        for j in range(1, i + 1):
            if i % j == 0:
                divisors_count += 1
        
        if divisors_count >= 3:
            composite_count += 1
    
    return composite_count
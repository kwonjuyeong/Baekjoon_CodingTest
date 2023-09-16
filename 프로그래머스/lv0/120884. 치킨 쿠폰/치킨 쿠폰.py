def solution(chicken):
    total_service = 0
    
    while chicken >= 10:
        service_chicken = chicken // 10
        total_service += service_chicken
        chicken = chicken % 10 + service_chicken
    
    return total_service    
    
    
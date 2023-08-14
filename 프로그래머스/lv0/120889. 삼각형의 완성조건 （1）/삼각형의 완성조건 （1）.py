def solution(sides):
    
    long = max(sides)
    if long < (sum(sides) - long):
        return 1
    else : return 2
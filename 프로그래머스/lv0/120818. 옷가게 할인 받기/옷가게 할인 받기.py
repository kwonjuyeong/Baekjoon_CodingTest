def solution(price):
    
    if 0 < price < 100000:
        return price
    elif 100000<= price < 300000 :
        return int(price *0.95)
    elif price < 500000 :
        return int(price *0.9)
    else : 
        return int(price *0.8)
    
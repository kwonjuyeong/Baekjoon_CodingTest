def solution(a, b):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    
    mother = b // gcd(a, b)
    
    while mother % 2 == 0:
        mother //= 2
    while mother % 5 == 0:
        mother //= 5
    
    if mother == 1:
        return 1
    else:
        return 2
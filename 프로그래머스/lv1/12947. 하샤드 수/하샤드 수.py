def solution(x):
    if x % add(x) == 0:
        return True
    else :
        return False
    
def add(n):
    sum = 0 
    if n<10:
        sum += n
        return sum
    else :
        return n%10+add(n//10)
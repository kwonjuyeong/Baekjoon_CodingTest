def solution(binomial):
    answer = 0
    
    sik = binomial.split()
    
    a = int(sik[0])
    op = sik[1]
    b = int(sik[2])
    
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    
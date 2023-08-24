def solution (n) : 
    fibonacci = [0, 1]

    for i in range(n-1):
        fibonacci.append(fibonacci[i] + fibonacci[i+1])
        
    return fibonacci[n] % 1234567
   
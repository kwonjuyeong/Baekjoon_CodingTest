A, B = map(int, input().split())

re = A*B

while B:
    if A > B:
        A, B = B, A
    B %= A
    
print(re//A)
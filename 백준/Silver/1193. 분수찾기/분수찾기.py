X = int(input())

K = 1
while X > K:
    X -= K
    K += 1
    
if K % 2 == 0:
    numerator = X
    denominator = K - X + 1
else:
    numerator = K - X + 1
    denominator = X

print(f"{numerator}/{denominator}")
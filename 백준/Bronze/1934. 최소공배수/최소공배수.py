# 유클리드 호재법
# a와 b의 최대 공약수를 구한다. 기존 수의 곱을 최대 공약수로 나누면 최대 공배수가 된다.

T = int(input())

def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

for _ in range(T):
    a, b = map(int, input().split())
    result = a * b // gcd(a, b)
    print(result)


#T = int(input())

#for _ in range(T):
#    i = 1
#    A, B = map(int, input().split())

#    while (i % A != 0) or (i % B != 0):
#        i += 1

#    print(i)
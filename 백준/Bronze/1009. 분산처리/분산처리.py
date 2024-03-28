import sys
input = sys.stdin.readline
T = int(input())
for i in range(T):
    a, b = map(int, input().split())
    b = b%4
    if b%4 ==0 :
        b = 4
    s = a**b
    if s%10 == 0:
        print(10)
    else:
        print(s%10)


#1
#T = int(input())
#for _ in range(T):
#    a, b = map(int, input().split())
#    print((a ** b) % 10)

#2
# 1 = 1, 1, 1, 1, 1, 1, 1
# 2 = 2^1 : 2, 2^2 : 4, 2^3 : 8, 2^4 : 16, 2^5 : 32, 2^6 = 64 ...  2, 4, 8, 6 반복
# 3 = 3^1 : 3, 3^2 : 9, 3^3 : 27, 3^4 : 81 = 3, 9, 7, 1 반복
# ....
# 9 = 9^1 : 9, 9^2 : 81, 9^3 : 729 = 9, 1 반복
N, B = map(int, input().split())
answer = ""

while N > 0:
    rem = N % B
    if rem < 10:
        answer = str(rem) + answer
    else:
        answer = chr(ord('A') + (rem - 10)) + answer
    N //= B

print(answer)
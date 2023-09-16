def solution(n):
    answer = 0
    i = n
    while True:
        if n < i and bin(n).count("1") == bin(i).count("1"):
            return i
            break
        else:
            i += 1
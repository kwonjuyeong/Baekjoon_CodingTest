def solution(n):
    ls = list(str(n))
    print(ls)
    ls.sort(reverse = True)
    print(ls)
    return int("".join(ls))
        
def solution(s):
    answer = True
    lists = []
    
    for i in s:
        if len(lists) == 0 and i == ")":
            return False
            break
        else:
            if i == "(":
                lists.append(i)
            else:
                if lists[-1] == "(":
                    lists.pop()
                else:
                    return False
    if len(lists) == 0:
        return True
    else:
        return False
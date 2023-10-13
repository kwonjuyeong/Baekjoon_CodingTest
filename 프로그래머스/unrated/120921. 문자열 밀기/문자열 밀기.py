def solution(A, B):
    if A == B:
        return 0
    
    A_list = list(A)
    B_list = list(B)
    
    for result in range(len(A)):
        if A_list == B_list:
            return result
        A_list.insert(0, A_list.pop())
    
    return -1
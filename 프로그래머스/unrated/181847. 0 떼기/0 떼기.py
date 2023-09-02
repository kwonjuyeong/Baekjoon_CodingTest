def solution(n_str):
    if n_str[0] == "0":
        return solution(n_str[1:])  
    else:
        return n_str
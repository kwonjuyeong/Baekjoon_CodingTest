def solution(code):
    ret = ''
    mode = 0
    
    for i in range(len(code)):
        if code[i] == "1":
            if mode == 0:
                mode = 1
            else:
                mode = 0
        else:
            if mode == 0:
                if i % 2 == 0:
                    ret += code[i]
            else:
                if i % 2 == 1:
                    ret += code[i]
    if ret == "":
        return "EMPTY"
    else:
        return ret
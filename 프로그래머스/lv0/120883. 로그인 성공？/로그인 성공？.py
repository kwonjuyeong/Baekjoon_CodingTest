def solution(id_pw, db):
    answer = ''
    
    for info in db:
        if id_pw[0] == info[0]:
            if id_pw[1] == info[1]:
                return "login"
            elif id_pw[1] != info[1]:
                return "wrong pw"
        
    return "fail"        
    
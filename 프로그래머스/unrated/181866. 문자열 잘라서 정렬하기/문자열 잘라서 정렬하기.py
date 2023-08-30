def solution(myString):
    answer = myString.split("x")
    
    non_empty = sorted([answer for answer in answer if answer != ""])
    
    return non_empty
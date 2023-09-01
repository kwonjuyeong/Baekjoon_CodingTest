def solution(myString, pat):
    convert = myString.replace("A", "x")
    transfer_list = convert.replace("B", "A").replace("x", "B")
    
    if pat in transfer_list:
        return 1
    else:
        return 0 

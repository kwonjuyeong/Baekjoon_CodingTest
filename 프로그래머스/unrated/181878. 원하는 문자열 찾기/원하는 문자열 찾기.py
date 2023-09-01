def solution(myString, pat):
    upperpat = pat.upper()
    uppermyString = myString.upper()
    
    
    
    if upperpat in uppermyString:
        return 1
    else:
        return 0
    
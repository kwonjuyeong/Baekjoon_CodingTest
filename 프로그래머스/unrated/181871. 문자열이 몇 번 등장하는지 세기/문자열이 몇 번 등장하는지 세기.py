def solution(myString, pat):

    word = ''
    count = 0
    
    for i in myString:
        word += i
        if word.endswith(pat):
            count += 1
    return count        
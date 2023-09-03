def solution(my_string):
    answer = ''
    
    for word in my_string:
        if word.islower():
            answer += word.upper()
        else:
            answer += word.lower()
    
    return answer
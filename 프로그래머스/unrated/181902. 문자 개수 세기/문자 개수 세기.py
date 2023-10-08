def solution(my_string):
    answer = []
    
    alphabets = [0]*52
    
    
    for word in my_string:
        if 'A' <= word <= 'Z':
            index = ord(word) - ord('A')
        elif 'a' <= word <= 'z':
            index = ord(word) - ord('a') + 26
        else:
            continue
        alphabets[index] += 1
    
    return alphabets
def solution(s, n):
    answer = ''
    
    for char in s:
        if char.isalpha():
            shift = n % 26
            if char.isupper():
                new_char = chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
            else:
                new_char = chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
        else:
            new_char = char
        answer += new_char
    
    return answer
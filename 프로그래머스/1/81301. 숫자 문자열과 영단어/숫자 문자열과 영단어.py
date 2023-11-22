def solution(s):
    result = ''
    alphabet = {"zero":"0", "one" : "1", "two" : "2", "three" : "3", "four" : "4", "five" : "5", "six" : "6", "seven" : "7", "eight" : "8", "nine" : "9"}
    word = ""

    for i in s:
        if i.isdigit():
            result += i
        else:
            word += i
            if word in alphabet:
                result += alphabet[word]
                word = ""

    if word in alphabet:
        result += alphabet[word]

    return int(result)
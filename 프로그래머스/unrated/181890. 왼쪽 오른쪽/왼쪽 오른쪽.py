def solution(str_list):
    
    for i in range(len(str_list)):
        if str_list[i] == "l":
            return str_list[:i]
        elif str_list[i] == "r":
            return str_list[i+1:]
    
    return []
    #word = ''.join(str_list)

    #for i in word:
    #    if 'l' not in word and 'r' not in word:
    #       return []
    #        break
    #    if i == 'l':
    #        answer = word.split("l")
    #        return list(answer[0])
    #        break
    #    elif i == 'r':
    #        answer = word.split("r")
    #        return list(answer[1])
    #        break 
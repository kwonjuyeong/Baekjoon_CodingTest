def solution(arr, k):
    result = []
    unique_dict = {}

    for num in arr:
        if num not in unique_dict:
            unique_dict[num] = True
    
    unique_list = list(unique_dict.keys())

    for i in range(k):
        if i < len(unique_list):
            result.append(unique_list[i])
        else:
            result.append(-1)
    
    return result
    
    
    
    
    
    #unique_list = list(set(arr))
    #for i in range(k):
    #    if i < len(unique_list):
    #        answer.append(unique_list[i])
    #    else:
    #        answer.append(-1)
            
    #return answer
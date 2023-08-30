def solution(arr, k):
    result = []
    
    for num in arr:
        if k % 2 == 1:  # 홀수
            result.append(num * k)
        else:  # 짝수
            result.append(num + k)
    
    return result
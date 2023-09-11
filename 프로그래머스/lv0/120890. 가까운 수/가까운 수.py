def solution(array, n):
    closeNum = None
    min_distance = float('inf')

    for num in array:
        distance = abs(num - n)
        if distance < min_distance or (distance == min_distance and num < closeNum):
            min_distance = distance
            closeNum = num
            
    return closeNum
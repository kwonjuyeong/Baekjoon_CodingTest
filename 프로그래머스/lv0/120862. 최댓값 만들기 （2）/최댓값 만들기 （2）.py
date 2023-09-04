def solution(numbers):
    numbers.sort()
    
    max1, max2 = numbers[-1], numbers[-2]
    min1, min2 = numbers[0], numbers[1]
    
    result1 = max1 * max2
    result2 = min1 * min2
    
    return max(result1, result2)
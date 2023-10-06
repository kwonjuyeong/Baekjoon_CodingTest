def solution(arr):
    seen = set()
    x = 0
    while tuple(arr) not in seen:
        seen.add(tuple(arr))
        for i in range(len(arr)):
            if arr[i] >= 50 and arr[i] % 2 == 0:
                arr[i] = arr[i] // 2
            elif arr[i] < 50 and arr[i] % 2 == 1:
                arr[i] = arr[i] * 2 + 1
        x += 1
    
    return x - 1
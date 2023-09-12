def solution(myString, pat):
    arr = []
    for i in range(len(myString)):
        arr.append(myString[i::-1])
    for j in range(len(arr)-1, -1, -1):
        if arr[j].startswith(pat[::-1]):
            return arr[j][::-1]
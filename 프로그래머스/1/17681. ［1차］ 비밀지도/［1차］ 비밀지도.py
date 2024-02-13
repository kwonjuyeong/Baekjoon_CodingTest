def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        row = bin(arr1[i] | arr2[i])[2:]  # 이진수 변환 후 맨 앞 '0b' 제거
        row = row.rjust(n, '0')  # 길이가 n이 될 때까지 왼쪽에 0으로 채움
        row = row.replace('1', '#')
        row = row.replace('0', ' ')
        answer.append(row)
    return answer
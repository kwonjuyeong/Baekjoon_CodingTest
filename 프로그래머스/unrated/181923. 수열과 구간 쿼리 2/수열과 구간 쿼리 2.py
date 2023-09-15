def solution(arr, queries):
    answer = []

    for query in queries:
        s, e, k = query
        sub_array = arr[s:e+1]
        sub_array.sort()
        result = -1

        # 부분 배열에서 k보다 크면서 가장 작은 값 찾기
        for num in sub_array:
            if num > k:
                result = num
                break

        answer.append(result)

    return answer
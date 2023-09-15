def solution(strArr):
    # 길이별 그룹을 저장할 딕셔너리
    length_groups = {}
    
    for s in strArr:
        length = len(s)
        if length not in length_groups:
            length_groups[length] = []
        length_groups[length].append(s)
    
    # 가장 개수가 많은 그룹의 크기 찾기
    max_group_size = 0
    for length, group in length_groups.items():
        max_group_size = max(max_group_size, len(group))
    
    return max_group_size
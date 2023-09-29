def solution(emergency):
    emergencyDic = {}
    copy_emergency = list(emergency)

    for i in range(len(emergency)):
        emergencyDic[max(emergency)] = i + 1
        emergency.remove(max(emergency))

    return [emergencyDic[value] for value in copy_emergency]
        
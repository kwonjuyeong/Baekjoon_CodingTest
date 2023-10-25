def solution(l, r):
    result = []

    for i in range(l, r + 1):
        digits = str(i)
        is_good_number = True

        for digit in digits:
            if digit not in ('0', '5'):
                is_good_number = False
                break

        if is_good_number:
            result.append(i)

    if result:
        return result
    else:
        return [-1]
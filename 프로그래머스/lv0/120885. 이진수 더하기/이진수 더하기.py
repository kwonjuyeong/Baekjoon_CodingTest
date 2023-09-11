def solution(bin1, bin2):
    # 두 이진수를 10진수로 변환 후 합산
    sum_decimal = int(bin1, 2) + int(bin2, 2)

    # 합산 결과를 다시 이진수로 변환하여 반환
    result = bin(sum_decimal)[2:]

    return result
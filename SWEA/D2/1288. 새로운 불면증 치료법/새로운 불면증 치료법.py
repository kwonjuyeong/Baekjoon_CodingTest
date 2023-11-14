T = int(input())

def count_digits(n):
    digits = set()
    count = 0
    while len(digits) < 10:  # 0부터 9까지의 모든 숫자를 보기 위한 조건
        count += 1
        current_number = n * count
        for digit in str(current_number):
            digits.add(digit)
    return count

for test_case in range(1, T + 1):
    N = int(input())
    result = count_digits(N)
    print(f'#{test_case} {result * N}')
T = int(input())

for test_case in range(1, T + 1):
    memory = input()
    count = 0
    current_bit = '0'

    for bit in memory:
        if bit != current_bit:
            count += 1
            current_bit = bit

    print(f'#{test_case} {count}')
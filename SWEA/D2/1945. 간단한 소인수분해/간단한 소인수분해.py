T = int(input())
li = [2, 3, 5, 7, 11]

for test_case in range(1, T + 1):
    N = int(input())
    num = [0] * 5 

    for i in range(5):
        while N % li[i] == 0:
            num[i] += 1
            N //= li[i]

    print(f'#{test_case} {" ".join(map(str, num))}')
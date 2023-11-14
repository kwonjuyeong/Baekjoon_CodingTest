T = int(input())
for test_case in range(1, T + 1):
    A, B = map(int, input().split())
    cnt = 0
    for i in range(A, B + 1):
        if str(i) == str(i)[::-1]:
            root = i ** 0.5
            int_root = int(root)
            if root == int_root and str(int_root) == str(int_root)[::-1]:
                cnt += 1
    print(f'#{test_case} {cnt}')
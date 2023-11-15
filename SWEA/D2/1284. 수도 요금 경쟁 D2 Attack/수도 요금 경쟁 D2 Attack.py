T = int(input())

for test_case in range(1, T + 1):
    P, Q, R, S, W = map(int, input().split())
    A_cost = P * W    
    if W <= R:
        B_cost = Q
    else:
        B_cost = Q + (W - R) * S
    
    result = min(A_cost, B_cost)
    print(f'#{test_case} {result}')
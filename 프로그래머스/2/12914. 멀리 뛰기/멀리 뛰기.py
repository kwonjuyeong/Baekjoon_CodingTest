def solution(n):
    dp = [1] + [0] * n
    dp[0], dp[1] = 1, 1
    for i in range(2, n+1):
        dp[i] = (dp[i-1] + dp[i-2]) % 1234567
    return dp[n]

    #1. 1칸 or 2칸 이동 가능
    #2. 총 칸 수 n
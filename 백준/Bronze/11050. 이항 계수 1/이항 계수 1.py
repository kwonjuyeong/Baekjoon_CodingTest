def facto(n):
    if n <= 1:
        return 1
    else:
        return n * facto(n-1)

N, K = map(int, input().split())

result = facto(N) // (facto(K) * facto(N-K))

print(result)
import sys

def sieve_of_eratosthenes(limit):
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False

    for p in range(2, int(limit**0.5) + 1):
        if sieve[p]:
            for i in range(p * p, limit + 1, p):
                sieve[i] = False

    return sieve

primes = sieve_of_eratosthenes(2 * 123456)  # 2 * 123456 범위 내의 소수를 미리 계산

while True:
    n = int(sys.stdin.readline().strip())
    if n == 0:
        break
    count = 0
    for i in range(n + 1, 2 * n + 1):
        if primes[i]:
            count += 1
    print(count)
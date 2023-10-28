count = int(input())
real = list(map(int, input().split()))
real.sort()
print(real[0]*real[-1])
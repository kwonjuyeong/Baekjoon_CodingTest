T = int(input())
numbers = list(map(int, input().split()))
numbers.sort()

print(numbers[T//2])
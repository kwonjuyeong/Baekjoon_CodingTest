def whoWins(N):
    if N % 2 == 0:
        return "Duck"
    else:
        return "Goose"

N = int(input())

result = whoWins(N)
print(result)
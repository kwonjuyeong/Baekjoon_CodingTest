pieces = list(map(int, input().split()))

correct_pieces = [1, 1, 2, 2, 2, 8]

result = [correct_pieces[i] - pieces[i] for i in range(6)]

print(*result)
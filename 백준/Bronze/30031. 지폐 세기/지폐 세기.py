N = int(input())
total_amount = 0

note_widths = {
    136: 1000,
    142: 5000,
    148: 10000,
    154: 50000 
}

for _ in range(N):
    width, height = map(int, input().split())
    total_amount += note_widths[width]

print(total_amount)
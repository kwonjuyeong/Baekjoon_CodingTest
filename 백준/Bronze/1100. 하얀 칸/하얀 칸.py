chess_board = [input().strip() for _ in range(8)]

white_pieces_count = 0
for i in range(8):
    for j in range(8):
        if (i + j) % 2 == 0 and chess_board[i][j] == 'F':
            white_pieces_count += 1

print(white_pieces_count)
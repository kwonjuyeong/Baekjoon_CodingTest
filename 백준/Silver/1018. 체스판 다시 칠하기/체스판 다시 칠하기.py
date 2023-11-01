n, m = map(int, input().split())
board = [] #전체 보드를 저장하는 리스트
result = [] # 색칠해야하는 결과를 나타내는 리스트
 
for _ in range(n):
    board.append(input()) #1 전체 보드를 저장해준다.
 
for i in range(n-7): #시작 지점을 지정해준다(-7은 시작점부터 마지막까지 구해야하는데, 인덱스가 넘어가면 안되기 때문이다)
    for j in range(m-7):
        turn_b = 0    #시작점이 검은 경우와 흰색일 경우를 대비해 두 가지 변수
        turn_w = 0
 
        for a in range(i, i+8):
            for b in range(j, j+8):
                if (a + b) % 2 == 0:
                    if board[a][b] != 'B':
                        turn_b += 1
                    if board[a][b] != 'W':
                        turn_w += 1
                else:
                    if board[a][b] != 'W':
                        turn_b += 1
                    if board[a][b] != 'B':
                        turn_w += 1
 
        result.append(turn_b)
        result.append(turn_w)

print(min(result))
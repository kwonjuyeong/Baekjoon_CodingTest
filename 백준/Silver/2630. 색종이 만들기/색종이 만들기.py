import sys

n = int(input())  # N*N 갯수 입력
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]  # N*N의 종이 색 입력(0과1로 이루어져 있음)
result = []  # 결과 값 출력

def papercut(x, y, N):  # 재귀 호출로 구분
    color = paper[x][y]  # 색은 입력받은 종이의 현재 좌표값
    for i in range(x, x + N):  # x좌표
        for j in range(y, y + N):  # y좌표
            if color != paper[i][j]:  # 현재 색과 다음 색이 다르면
                papercut(x, y, N // 2)  # 종이 나누기
                papercut(x, y + N // 2, N // 2)
                papercut(x + N // 2, y, N // 2)
                papercut(x + N // 2, y + N // 2, N // 2)
                return
    if color == 0:
        result.append(0)
    else:
        result.append(1)

papercut(0, 0, n)
print(result.count(0))
print(result.count(1))
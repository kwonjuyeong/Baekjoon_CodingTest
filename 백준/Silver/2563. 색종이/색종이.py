# 흰색 도화지를 100x100 크기의 2차원 배열로 초기화
canvas = [[0] * 100 for _ in range(100)]

# 색종이의 수 입력
num_papers = int(input())

# 색종이를 도화지에 붙이기
for _ in range(num_papers):
    x, y = map(int, input().split())
    for i in range(x, x + 10):
        for j in range(y, y + 10):
            canvas[i][j] = 1

# 검은 영역의 넓이 계산
black_area = sum(row.count(1) for row in canvas)

print(black_area)
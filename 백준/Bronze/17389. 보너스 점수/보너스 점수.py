N = int(input())
S = list(input())

total_score = 0  # 총 점수를 저장하는 변수
bonus_score = 0  # 보너스 점수를 저장하는 변수

for i in range(N):
    if S[i] == 'O':
        total_score += (i + 1) + bonus_score
        bonus_score += 1
    else:
        bonus_score = 0

print(total_score)
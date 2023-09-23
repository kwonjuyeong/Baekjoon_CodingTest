N = int(input())
scores = list(map(int, input().split()))
max_score = max(scores)
sum_score = 0

for score in scores:
    sum_score += (score / max_score) * 100
    
average_score = sum_score/N    

print(average_score)
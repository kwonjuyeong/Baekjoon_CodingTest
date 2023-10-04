total_credit = 0
total_score = 0

for _ in range(20):
    name, credit, grade = input().split()
    credit = float(credit)
    
    if grade == 'A+':
        score = 4.5
    elif grade == 'A0':
        score = 4.0
    elif grade == 'B+':
        score = 3.5
    elif grade == 'B0':
        score = 3.0
    elif grade == 'C+':
        score = 2.5
    elif grade == 'C0':
        score = 2.0
    elif grade == 'D+':
        score = 1.5
    elif grade == 'D0':
        score = 1.0
    elif grade == 'F':
        score = 0.0
    else:
        score = 0.0
    
    if grade != 'P':
        total_score += score * credit
        total_credit += credit
        
result = total_score / total_credit

print(result)
        
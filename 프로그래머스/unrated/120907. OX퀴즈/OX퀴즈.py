def solution(quiz):
    result = []
    
    for expression in quiz:
        parts = expression.split()
        X, operator, Y, equals, Z = parts
        
        X, Y, Z = int(X), int(Y), int(Z)

        if operator == '+':
            result.append('O' if X + Y == Z else 'X')
        elif operator == '-':
            result.append('O' if X - Y == Z else 'X')
    
    return result
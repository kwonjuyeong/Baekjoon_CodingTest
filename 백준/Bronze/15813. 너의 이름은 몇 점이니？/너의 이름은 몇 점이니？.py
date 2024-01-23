def calculate_name_score(name):
    score = 0
    for char in name:
        if 'A' <= char <= 'Z':
            score += ord(char) - ord('A') + 1
    return score

name_length = int(input())
name = input().strip()

result = calculate_name_score(name)
print(result)
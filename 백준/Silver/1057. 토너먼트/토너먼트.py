N, jimin, hansu = map(int, input().split())

result = 0
while jimin != hansu:
	jimin -= jimin//2
	hansu -= hansu//2
	result += 1
print(result)
N = int(input())

dance = ["ChongChong"]

for _ in range(N):
	A, B = input().split()
	if A in dance:
		dance.append(B)
	elif B in dance:
		dance.append(A)
	else:
		continue

dance = set(dance)
print(len(dance))
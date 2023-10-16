gak = []

for i in range(3):
	n = int(input())
	gak.append(n)

if sum(gak) == 180:
	if len(set(gak)) == 1:
		print("Equilateral")
	elif len(set(gak)) == 2:
		print("Isosceles")
	else:
		print("Scalene")
else:
	print("Error")
N = int(input())

members = []

for _ in range(N):
    age, name = input().split()
    members.append([age, name])

members.sort(key=lambda x:int(x[0]))

for age, name in members:
	print(age, name)

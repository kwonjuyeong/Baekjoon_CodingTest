N, M = map(int, input().split())

students = [int(input()) for _ in range(N)]

for i in range(M):
    for j in range(N - 1):
        if students[j] % (i + 1) > students[j + 1] % (i + 1):
            students[j], students[j + 1] = students[j + 1], students[j]

for student in students:
    print(student)
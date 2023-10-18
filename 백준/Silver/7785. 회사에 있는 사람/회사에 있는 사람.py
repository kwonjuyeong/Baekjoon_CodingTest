N = int(input())

log = {}
for _ in range(N):
    name, state = input().split()
    log[name] = state

current_employees = [name for name, state in log.items() if state == "enter"]

# 정렬 후 역순으로 출력
current_employees.sort(reverse=True)

for employee in current_employees:
    print(employee)
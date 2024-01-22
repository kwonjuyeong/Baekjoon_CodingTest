import sys

N = int(input())
times = []
max_meeting = 1

for i in range(N):
    times.append(list(map(int, sys.stdin.readline().split())))
    
times.sort(key = lambda x: (x[1], x[0]))
end_time = times[0][1]

for j in range(1, N):
    if end_time <= times[j][0]:
        max_meeting += 1
        end_time = times[j][1]

print(max_meeting)
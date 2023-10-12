N, k = map(int, input().split())
people = list(map(int, input().split()))

people.sort()
cut_line = people[N - k]

print(cut_line)
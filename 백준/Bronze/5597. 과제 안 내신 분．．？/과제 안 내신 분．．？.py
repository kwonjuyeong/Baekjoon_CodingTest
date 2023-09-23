num = [i for i in range(1, 31)]

for _ in range(28):
    data = int(input())
    num.remove(data)
print(min(num))
print(max(num))


#go_students = set()
#for _ in range(28):
#    go_students.add(int(input()))

#all_students = set(range(1, 30))

#missing = all_students - go_students
#sorted_missing = sorted(list(missing))

#print(sorted_missing)







#go_students = set()

#for _ in range(27):
#    go_students.add(int(input()))

#all_students = set(range(1, 30))

#missing = all_students - go_students
#sorted_missing = sorted(list(missing))

#print(sorted_missing)


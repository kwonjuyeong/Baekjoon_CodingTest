n = int(input())
li = []

for i in range(1, n + 1):
    if n % i == 0:
        li.append(str(i)) 

print(" ".join(li))
word = input()
count = 0
i = 0

while i < len(word):
    if word[i:i+3] == "dz=":
        i += 3
    elif word[i:i+2] in ["c=", "c-", "d-", "lj", "nj", "s=", "z="]:
        i += 2
    else:
        i += 1
    count += 1
    
print(count)
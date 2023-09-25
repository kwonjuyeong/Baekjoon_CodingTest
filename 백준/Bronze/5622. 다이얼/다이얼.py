Number = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

input_number = list(input())
time = 0

for i in input_number:
    for j in Number:
        if i in j:
            #+3은 전화기에 ABC는 2이고 인덱스는 0부터 시작하기 때문(+2) 그리고 처음 2초가 걸리기 때문(+1)
            time += Number.index(j) + 3

print(time)            
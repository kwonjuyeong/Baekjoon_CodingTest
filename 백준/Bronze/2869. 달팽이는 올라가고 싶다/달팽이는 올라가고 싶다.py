A, B, V = map(int, input().split())

day = (V-B)/(A-B)

if day != int(day):
    day = int(day)+1
else:
    day = int(day)
    
print(day)


#A, B, V = map(int, input().split())

#move = 0
#day = 0

#while True:
#    day += 1
#    move += A
#    if move >= V:
#        break
#    move -= B

#print(day)
from collections import deque

N = int(input())
card = deque(range(1, N+1))
while len(card) != 1:
    card.popleft()
    card.append(card.popleft())
print(card.popleft())



#N = int(input())
#card = list(range(1, N + 1))

#while len(card) != 1:
#    card.pop(0)
#    card.append(card.pop(0))

#print(card[0])
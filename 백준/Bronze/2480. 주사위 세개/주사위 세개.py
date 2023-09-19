dice = list(map(int, input().split()))
unique_dice = set(dice)

if len(unique_dice) == 1:
    prize = 10000 + list(unique_dice)[0] * 1000
elif len(unique_dice) == 2:
    for num in unique_dice:
        if dice.count(num) == 2:
            prize = 1000 + num * 100
            break
else:
    prize = max(dice) * 100

print(prize)
def calculate_width(number):
    width = 0
    for digit in number:
        if digit == '1':
            width += 2
        elif digit == '0':
            width += 4
        else:
            width += 3
    return width + len(number) - 1 + 2

while True:
    number = input()
    if number == '0':
        break
    print(calculate_width(number))
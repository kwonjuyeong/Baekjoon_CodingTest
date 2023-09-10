def solution(my_string):
    num = ""
    total = 0

    for char in my_string:
        if char.isdigit():
            num += char
        elif num:
            total += int(num)
            num = ""

    if num:
        total += int(num)

    return total
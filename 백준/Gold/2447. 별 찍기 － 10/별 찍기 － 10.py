def stars(n):
    if n == 1:
        return ['*']

    Stars = stars(n // 3)
    line = []

    for star in Stars:
        line.append(star * 3)
    for star in Stars:
        line.append(star + ' ' * (n // 3) + star)
    for star in Stars:
        line.append(star * 3)

    return line

N = int(input())
print('\n'.join(stars(N)))
values = {'black' : 0, 'brown': 1, 'red': 2, 'orange': 3, 'yellow': 4, 'green': 5, 'blue': 6, 'violet': 7, 'grey': 8, 'white': 9}

value_color1 = input()
value_color2 = input()
multiply_color = input()

print(int(str(values[value_color1]) + str(values[value_color2])) * (10**values[multiply_color]))
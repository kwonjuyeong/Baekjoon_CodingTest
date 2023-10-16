while True:
    square_list = sorted(list(map(int, input().split())))
    if square_list[0] == 0 and square_list[1] == 0 and square_list[2] == 0:
        break
    else:
        if square_list[2] < square_list[0] + square_list[1]:
            if len(set(square_list)) == 1:
                print("Equilateral")
            elif len(set(square_list)) == 2:
                print("Isosceles")
            else:
                print("Scalene")
        else:
            print("Invalid")
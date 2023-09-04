def solution(box, n):
    x_count = box[0] // n
    y_count = box[1] // n
    z_count = box[2] // n
    
    return x_count * y_count * z_count
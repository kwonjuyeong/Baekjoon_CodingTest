def solution(hp):
    king = hp//5
    hp = hp % 5
    
    soldiers = hp // 3
    hp %= 3

    return king + soldiers + hp
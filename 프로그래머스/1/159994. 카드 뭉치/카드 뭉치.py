def solution(cards1, cards2, goal):
    answer = ''
    goal_index = 0
    c1_index = 0
    c2_index = 0
    
    while goal_index < len(goal):
        if c1_index < len(cards1) and cards1[c1_index] == goal[goal_index]:
            c1_index += 1
        elif c2_index < len(cards2) and cards2[c2_index] == goal[goal_index]:
            c2_index += 1
        else:
            break
        goal_index += 1
        
    if goal_index == len(goal):
        return "Yes"
    else:
        return "No"
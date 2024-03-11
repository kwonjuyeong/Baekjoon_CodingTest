def solution(s):
    answer = 0
    s = list(s)
    
    for _ in range(len(s)):
        stacks = []
        for i in range(len(s)):
            if len(stacks) > 0:
                if stacks[-1] == '[' and s[i] == ']': stacks.pop()
                elif stacks[-1] == '{' and s[i] == '}': stacks.pop()
                elif stacks[-1] == '(' and s[i] == ')': stacks.pop()
                else:
                    stacks.append(s[i])
            else:
                stacks.append(s[i])
        if len(stacks) == 0:
            answer += 1
        s.append(s.pop(0))

        
    return answer
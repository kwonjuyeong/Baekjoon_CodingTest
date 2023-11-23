from collections import Counter

def solution(array):
    count = Counter(array)
    max_count = max(count.values())
    modes = [num for num, freq in count.items() if freq == max_count]

    if len(modes) > 1:
        return -1
    else:
        return modes[0] if modes else -1
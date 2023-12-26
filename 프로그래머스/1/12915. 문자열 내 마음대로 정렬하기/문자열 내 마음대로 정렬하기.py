def solution(strings, n):
    def sort_key(item):
        return item[n], item

    strings.sort(key=sort_key)
    return strings
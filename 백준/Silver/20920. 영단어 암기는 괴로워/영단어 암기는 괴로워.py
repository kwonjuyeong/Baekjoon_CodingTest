import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
word_list = {}

for _ in range(N):
    word = sys.stdin.readline().rstrip()
    if len(word) >= M:
        if word in word_list:
            word_list[word] += 1
        else:
            word_list[word] = 1

sorted_word_list = sorted(word_list.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))

for word, count in sorted_word_list:
    print(word)
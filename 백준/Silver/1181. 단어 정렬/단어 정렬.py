N = int(input())

words = set()

for _ in range(N):
	words.add(input())

word_list = list(words)

#길이 순, 단어 순
word_list.sort(key=lambda x: (len(x), x))

for word in word_list:
	print(word)
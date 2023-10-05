word_list = []

for _ in range(5):
    word = input()
    word_list.append(word)

max_len = max(len(word) for word in word_list)
result = ''

for i in range(max_len):
    for j in range(5):
        if i < len(word_list[j]):
            result += word_list[j][i] 
print(result)      
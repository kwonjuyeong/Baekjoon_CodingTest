def solution(n, words):
    used_words = set()
    prev_word = words[0]
    used_words.add(prev_word)
    
    for i in range(1, len(words)):
        word = words[i]
        if word in used_words or prev_word[-1] != word[0]:
            return [(i % n) + 1, (i // n) + 1]
        used_words.add(word)
        prev_word = word

    return [0, 0]
word = input().upper()
alphabet = [0] * 26

for i in word:
    if 'A' <= i <= 'Z':
        index = ord(i) - ord('A')
        alphabet[index] += 1
        
max_count = max(alphabet)

if alphabet.count(max_count) > 1:
    print("?")  # 최빈값이 여러 개인 경우
else:
    max_index = alphabet.index(max_count)  # 최빈 알파벳의 인덱스
    most_frequent_char = chr(max_index + ord('A'))  # 대문자로 변환
    print(most_frequent_char)        
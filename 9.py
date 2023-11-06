import string

print("Введите текст. Для завершения ввода введите пустую строку.")

text = []
words_frequency = {}
order_of_words = []
while True:
    line = input()
    if line:
        text.extend(line.translate(str.maketrans('', '', string.punctuation)).lower().split())
    else:
        break

for word in text:
    if word not in words_frequency:
        words_frequency[word] = 0
        order_of_words.append(word)
    words_frequency[word] += 1

sorted_words = sorted(order_of_words, key=lambda word: (-words_frequency[word], order_of_words.index(word)))

for word in sorted_words:
    print(word)

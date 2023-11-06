import string

sentence = input("Введите предложение: ")
sentence = sentence.translate(str.maketrans('', '', string.punctuation))
words = sentence.split()
print(set(words))

words = input('Please, enter some words: ').split()
for i in range(len(words)):
    if len(words[i]) > 10:
        words[i] = words[i][:10]
for m in enumerate(words, 1):
    print(m)
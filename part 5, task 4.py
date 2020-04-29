vocabulary = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре', 'Five': 'Пять', 'Six': 'Шесть',
              'Seven': 'Семь', 'Eight': 'Восемь', 'Nine': 'Девять', 'Ten': 'Десять'}

with open('text_4.txt', encoding='utf-8') as cool_in:
    with open('text_4-1.txt', 'w', encoding='utf-8') as cool_out:
        for line in cool_in:
            first, other = line.split(maxsplit=1)
            cool_out.write(vocabulary[first] + ' ' + other)

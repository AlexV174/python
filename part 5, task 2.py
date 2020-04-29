with open("text_2.txt", "r") as cool:
    lines = 0
    words = 0
    for i in cool:
        lines += 1
        words += len(i.split())
print(f"Количество строк в файле: {lines}")
print(f"Количество слов в файле: {words}")

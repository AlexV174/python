from functools import reduce

with open('text_5.txt', 'w') as f:
    f.write(" ".join([str(i) for i in range(1, 101,)]))

with open('text_5.txt', 'r') as f:
    result = reduce(lambda acc, line: int(acc) + int(line), f.readline().split())
    print(result)
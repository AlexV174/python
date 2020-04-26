from math import factorial
from itertools import count


def fibo_gen():
    for el in count(1):
        yield factorial(el)


genit = fibo_gen()
n = 0
for i in genit:
    if n < 15:
        print(i)
        n += 1
    else:
        break
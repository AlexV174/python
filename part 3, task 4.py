def my_pow(x, y):
    res = 1
    sec = abs(y)
    while sec > 0:
        res = res / x
        sec = sec - 1
    return res


x = abs(float(input('Введите число "x", которое хотите возвести в степень: ')))
y = int(input('Введите отрицательное число "y" (степень): '))
print(f'Возведение числа "x" в степень "y": {round((my_pow(x, y)),2)}')

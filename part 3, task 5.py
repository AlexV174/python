def m_sum(*args):
    sum_1 = 0
    n = True
    while n:
        number = input('Пожалуйста, введите числа через пробел или нажмите "Q" для выхода: ').split()
        res = 0
        for el in range(len(number)):
            if number[el] == 'q' or number[el] == 'Q':
                n = False
                break
            else:
                res = res + int(number[el])
        sum_1 = sum_1 + res
        print(f'Ваша сумма: {sum_1}')
    print(f'Итоговая сумма {sum_1}')


m_sum()

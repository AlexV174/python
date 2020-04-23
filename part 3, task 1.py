def my_f(*args):
    try:
        arg_1 = int(input('Введите число № 1 (делимое): '))
        arg_2 = int(input('Введите число № 2 (делитель): '))
        res = round(arg_1 / arg_2, 2)
    except ValueError:
        return 'Введите число ! (например: 1, 2, 3 ...)'
    except ZeroDivisionError:
        return 'Вы забыли? На "0" делить нельзя !'
    return res


print(my_f())

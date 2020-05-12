class ZerdiError(Exception):
    def __init__(self, msg):
        self.msg = msg


def division(a, b):
    if b == 0:
        raise ZerdiError('Деление на "0"! Операция не может быть выполнена !')

    return a / b


def main():
    print('Деление числа 1 на число 2')
    a = float(input('Введите делимое число (1): '))
    b = float(input('Введите делитель (2): '))
    try:
        print('Результат', division(a, b))
    except ZerdiError as e:
        print(e)


main()

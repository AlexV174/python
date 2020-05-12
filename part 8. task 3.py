class NotIntNumberError(Exception):
    def __init__(self, msg):
        self.msg = msg


def main():
    nums = []
    while True:
        s = input('Введите целочисленное значение или команду "stop" для завершения: ')
        if s == 'stop':
            break

        try:
            error = True
            if len(s) > 0:
                if s.isdigit():
                    error = False
                elif s[0] == '-' and s[1:].isdigit():
                    error = False

            if error:
                raise NotIntNumberError('Проверьте свой ввод! Нужно вводить только целочисленое значение!')

            nums.append(int(s))
        except NotIntNumberError as e:
            print(e)

    print(nums)


main()

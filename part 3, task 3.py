def sum_two(*args):
    try:
        arg_1 = int(input('Введите первое число: '))
        arg_2 = int(input('Введите второе число: '))
        arg_3 = int(input('Введите третье число: '))
        nums = [arg_1, arg_2, arg_3]
        max_1 = max(nums)
        nums.remove(max_1)
        max_2 = max(nums)
        return max_1 + max_2
    except ValueError:
        return 'Введите число !'


print(sum_two())

#def max_two(arg_1, arg_2, arg_3):
#    if arg_1 >= arg_2 and arg_2 >= arg_3:
#        return arg_1 + arg_2
#    elif arg_2 >= arg_1 and arg_3 > arg_1:
#        return arg_2 + arg_3
#    else:
#        return arg_1 + arg_3
#
#
#print(
#    f'Сумма двух чисел: {max_two(int(input("Введите первое число: ")), int(input("Введите второе число: ")), int(input("Введите третье число: ")))}')

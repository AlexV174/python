my_list = list(input('Введите элементы списка через пробел: ').split())
print('Вы ввели: ', my_list)
n = 0
for i in range(int(len(my_list)/2)):
    my_list[n], my_list[n+1] = my_list[n+1], my_list[n]
    n += 2
print(my_list)
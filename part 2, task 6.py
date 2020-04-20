my_list = []
names = []
costs = []
amounts = []
units = []
i = 1
while True:
    if input('Хотите внести новый товар? (да/нет): ') == 'да':
        name = input('Введите название товара: ')
        names.append(name)
        cost = input('Введите стоимость товара (руб.): ')
        costs.append(cost)
        amount = input('Введите количество товара: ')
        amounts.append(amount)
        unit = input('Введите единицу измерения товара: ')
        units.append(unit)
        my_list.append((i, {'Название': name, 'Стоимость': cost, 'Количество': amount, 'Ед.': unit}))
    else:
        break
    i += 1
for i in my_list:
    print(i)
print('<><><><><><><><><><><>')
my_dict = {'Название': names, 'Стоимость': costs, 'Количество': amounts, 'Ед.': units}
for keys, values in my_dict.items():
    print(f'{keys} - {values}')
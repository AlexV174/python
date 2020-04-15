revenue = float(input('Введите данные по выручке: '))
expenses = float(input('Введите данные по затратам: '))
if revenue > expenses:
    print('Детяльность Вашей фирмы прибыльная')
    rent = ((revenue - expenses) / revenue)
    print('Рентабельность Вашей фирмы равна:', rent)
    personal = float(input('Введите количество сотрудников: '))
    print('Прибыль Вашей фирмы в расчете на 1 сотрудника составляет:', revenue / personal)
elif revenue < expenses:
    print('Детяльность Вашей фирмы убыточная')
else:
    print('Ваша фирма работает в "0"')

def my_personal(name, surname, birthyear, citi, mail, tel):
    """ Функция предлагат ввести вользователю персональные данные"""
    print(
        f'Имя - {name}, Фамиля - {surname}, Год рождения - {birthyear}, Город проживания - {citi}, Электронная почта - '
        f'{mail}, Телефон - {tel}')


my_personal(name='Алексей', surname='Винокуров', birthyear='1991', citi='Златоуст', mail='viny_174@mail.ru',
            tel="89642443000")

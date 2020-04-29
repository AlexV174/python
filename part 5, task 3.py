def main():
    employees = {}

    with open('text_3.txt', encoding='utf-8') as cool:
        for num, line in enumerate(cool):
            name, salary = line.split()
            employees[name] = float(salary)

    print('Сотрудники, с заработной платой менее 20 000 руб.: ', [k for k, v in employees.items() if v < 20000])
    print(f'Средняя заработная плата сотрудников: {sum(employees.values()) / len(employees):.2f} руб.')


if __name__ == "__main__":
    main()

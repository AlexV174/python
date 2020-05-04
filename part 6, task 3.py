class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        return f'{self.surname} {self.name}'

    def get_total_income(self):
        return f'{self._income["wage"] + self._income["bonus"]}'


position = Position("Alexey", "Vinokuov", "Lawyer", 50000, 20000)

print(position.name)
print(position.surname)
print(position.position)
print(position._income)
print(position.get_full_name())
print(position.get_total_income())

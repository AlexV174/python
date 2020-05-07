class Cell:
    def __init__(self, cell_count):
        self._cell_count = None
        self.cell_count = cell_count

    def __str__(self):
        return f'{self._cell_count}'

    @property
    def cell_count(self):
        return self._cell_count

    @cell_count.setter
    def cell_count(self, count):
        try:
            int(count)
        except Exception as ex:
            print(f'Количество ячеек в клетке должно быть целочисленным ! {ex}')
        else:
            self._cell_count = int(count)

    def __add__(self, other):
        return Cell(self._cell_count + other.cell_count)

    def __sub__(self, other):
        result = self._cell_count - other.cell_count
        if result > 0:
            return Cell(result)
        else:
            print('Не может быть меньше " 1 " !')

    def __mul__(self, other):
        return Cell(self._cell_count * other.cell_count)

    def __truediv__(self, other):
        result = self._cell_count // other.cell_count
        return Cell(result) if result > 0 else print('Не может быть меньше " 1 " !')

    def make_order(self, line_count):
        cells = ''
        cell_line = 1
        for __ in range(self._cell_count):
            if cell_line > line_count:
                cells += '\n'
                cell_line = 1
            cells += '*'
            cell_line += 1
        return cells


cell_1 = Cell(40)
cell_2 = Cell(30)

print('Складываем: \n')
result_cell = cell_1 + cell_2
print(f'{cell_1.cell_count} + {cell_2.cell_count} = {result_cell}')

print('\nВычитаем: \n')
result_cell = cell_2 - cell_1
print(f'{cell_2.cell_count} - {cell_1.cell_count} = {result_cell}')

result_cell = cell_1 - cell_2
print(f'{cell_1.cell_count} - {cell_2.cell_count} = {result_cell}')

print('\nУмножаем: \n')
result_cell = cell_1 * cell_2
print(f'{cell_1.cell_count} * {cell_2.cell_count} = {result_cell}')

print('\nДелим: \n')

result_cell = cell_2 / cell_1
print(f'{cell_2.cell_count} / {cell_1.cell_count} = {result_cell}')

result_cell = cell_1 / cell_2
print(f'{cell_1.cell_count} / {cell_2.cell_count} = {result_cell}')

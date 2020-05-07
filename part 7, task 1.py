class Matrix():

    def my_func(self, a, b):
        return a + b

    def __init__(self, argv):
        self.matrix = argv

    def __str__(self):
        strs = ''
        for el in self.matrix:
            strs += '|' + '\t|'.join(map(str, el)) + '|\n'
        return strs

    def __add__(self, other):
        result = []
        try:
            for ex, ey in map(lambda *x: x, self.matrix, other.matrix):
                result.append(list(map(lambda x, y: x + y, ex, ey)))
        except Exception as ex:
            print(f'Разная размерность ! {ex}')
        else:
            return Matrix(result)


simple_matrix = [[3, 5, 32], [2, 4, 6], [-1, 64, -8]]
simple_matrix_1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix_1 = Matrix(simple_matrix)
matrix_2 = Matrix(simple_matrix_1)
print('Матрица 1: \n')
print(matrix_1)
print('Матрица 2: \n')
print(matrix_2)

matrix_3 = matrix_1 + matrix_2

print('Сложение матриц: \n')
print(matrix_3)

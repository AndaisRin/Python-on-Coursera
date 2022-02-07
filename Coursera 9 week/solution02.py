# Добавьте в предыдущий класс следующие методы:
# - __add__, принимающий вторую матрицу того же размера и возвращающий сумму матриц.
# - __mul__, принимающий число типа int или float и возвращающий матрицу, умноженную на скаляр.
# - __rmul__, делающий то же самое, что и __mul__. Этот метод будет вызван в том случае, аргумент находится справа. Для реализации этого метода в коде класса достаточно написать __rmul__ = __mul__.


from sys import stdin
from copy import deepcopy


class Matrix:

    def __init__(self, list_matrix=None):
        if list_matrix is None:
            list_matrix = []
        self.list_matrix = deepcopy(list_matrix)

    def __str__(self):
        str_el = ''
        for elem in self.list_matrix:
            str_el += '\t'.join(map(str, elem)) + '\n'
        return str_el[:-1]

    def size(self):
        return len(self.list_matrix), len(self.list_matrix[0])

    def __add__(self, other):
        ri, rj = range(len(self.list_matrix)), range(len(self.list_matrix[0]))
        return Matrix(
            [[self.list_matrix[i][j] + other.list_matrix[i][j]
              for j in rj] for i in ri])

    def __mul__(self, other):
        ri, rj = range(len(self.list_matrix)), range(len(self.list_matrix[0]))
        return Matrix(
            [[self.list_matrix[i][j] * other for j in rj] for i in ri])

    __rmul__ = __mul__


#exec(stdin.read())
m1 = Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
m2 = Matrix([[0, 1, 0], [20, 0, -1], [-1, -2, 0]])
print(m1 + m2)

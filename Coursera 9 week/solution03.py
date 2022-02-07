# Добавьте в программу из предыдущей задачи класс MatrixError, содержащий внутри self поля matrix1 и matrix2 — ссылки на матрицы.
# В класс Matrix внесите следующие изменения:
# - Добавьте в метод __add__ проверку на ошибки в размере входных данных, чтобы при попытке сложить матрицы разных размеров было выброшено исключение MatrixError таким образом, чтобы matrix1 поле MatrixError стало первым аргументом __add__ (просто self), а matrix2  —  вторым (второй операнд для сложения).
# - Реализуйте метод transpose, транспонирующий матрицу и возвращающую результат (данный метод модифицирует экземпляр класса Matrix)
# - Реализуйте статический метод transposed, принимающий Matrix и возвращающий транспонированную матрицу.

from sys import stdin
from copy import deepcopy


class MatrixError(BaseException):
    def __init__(self, Matrix, other):
        self.matrix1 = Matrix
        self.matrix2 = other


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

    def __add__(self, other):
        if len(self.list_matrix) == len(other.list_matrix) and len(
                self.list_matrix[0]) == len(other.list_matrix[0]):
            ri, rj = range(len(self.list_matrix)), range(
                len(self.list_matrix[0]))
            return Matrix(
                [[self.list_matrix[i][j] + other.list_matrix[i][j]
                  for j in rj] for i in ri])
        else:
            raise MatrixError(self, other)

    def __mul__(self, other):
        ri, rj = range(len(self.list_matrix)), range(len(self.list_matrix[0]))
        return Matrix(
            [[self.list_matrix[i][j] * other for j in rj] for i in ri])

    __rmul__ = __mul__

    def size(self):
        return len(self.list_matrix), len(self.list_matrix[0])

    def transpose(self):
        ri, rj = range(len(self.list_matrix)), range(len(self.list_matrix[0]))
        transpose_matrix = [[self.list_matrix[j][i] for j in ri] for i in rj]
        self.list_matrix = transpose_matrix
        return Matrix(self.list_matrix)

    @staticmethod
    def transposed(other):
        ri, rj = range(len(other.list_matrix)), range(
            len(other.list_matrix[0]))
        return Matrix([[other.list_matrix[i][j] for i in ri] for j in rj])


exec(stdin.read())

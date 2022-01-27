# На вход подаётся последовательность натуральных чисел длины n≤1000.Посчитайте произведение пятых степеней чисел в последовательности.
from functools import reduce

print(reduce(lambda x, y: x * y, map(lambda x: x ** 5, map(int, input().split()))))

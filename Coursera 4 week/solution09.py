def min_divisor(n):
    if n % 2 == 0:
        return 2
    i = 3
    while n % i != 0 and i * i <= n:
        i += 2
    if i * i <= n:
        return i
    return n


# Дано натуральное число n>1. Выведите его наименьший делитель, отличный от 1. 
# Решение оформите в виде функции MinDivisor(n).
# Алгоритм должен иметь сложность порядка корня квадратного из n.
x = int(input())
print(min_divisor(x))

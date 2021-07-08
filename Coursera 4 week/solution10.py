def min_divisor(n):
    if n % 2 == 0:
        return 2
    i = 3
    while n % i != 0 and i * i <= n:
        i += 2
    if i * i <= n:
        return i
    return n


def is_prime(n):
    return 'YES' if n == min_divisor(n) else 'NO'


# Дано натуральное число n>1. Проверьте, является ли оно простым.
# Программа должна вывести слово YES, если число простое и NO, если число составное.
# Решение оформите в виде функции IsPrime(n), которая возвращает True для простых чисел и False для составных чисел.
x = int(input())
print(is_prime(x))

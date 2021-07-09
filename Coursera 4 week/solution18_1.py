def factorial(a):
    if a > 1:
        a = a * factorial(a - 1)
    return a


def cnk(n, k):
    if k == 1:
        return n
    elif n == k or k == 0:
        return 1
    else:
        return int(factorial(n) / (factorial(n - k) * factorial(k)))


# По данным целым числам n и k  (0≤k≤n) вычислите C из n по k.
# Решение оформите в виде функции C(n, k).
x, y = int(input()), int(input())
print(cnk(x, y))

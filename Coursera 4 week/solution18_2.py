def cnk(n, k):
    if k == 1:
        return n
    elif n == k or k == 0:
        return 1
    else:
        return cnk(n - 1, k) + cnk(n - 1, k - 1)


# По данным целым числам n и k  (0≤k≤n) вычислите C из n по k.
# Решение оформите в виде функции C(n, k).
x, y = int(input()), int(input())
print(cnk(x, y))

def power(a, n):
    return a**n

# Дано действительное положительное число a и целоe число n.
# Вычислите aⁿ. Решение оформите в виде функции power(a, n).
# Стандартной функцией возведения в степерь пользоваться нельзя.
# Примечания Здесь не нужна рекурсия.
x, y = float(input()), int(input())
print(power(x, y))
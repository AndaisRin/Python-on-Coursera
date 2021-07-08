def power(a, n):
    if n == 0:
        a = 1
    if n % 2 == 0 and n >= 1:
        a = power(a * a, n / 2)
    if n % 2 != 0 and n >= 1:
        a = a * power(a, n - 1)
    return a


# Реализуйте алгоритм быстрого возведения в степень.
# Для этого нужно воспользоваться следующими рекуррентными соотношениями:
# aⁿ = (a²)ⁿ/² при четном n, aⁿ=a⋅aⁿ⁻¹ при нечетном n.
x, y = float(input()), int(input())
print(power(x, y))

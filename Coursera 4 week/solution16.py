def gcd(a, b):
    if not (a != 0 and b != 0):
        return a + b
    if a > b:
        a = a % b
    else:
        b = b % a
    return gcd(a, b)


def reduce_fraction(a, b):
    gcd(a, b)
    return a // gcd(a, b), b // gcd(a, b)


# Сократите дробь (n / m), то есть выведите два других числа p и q таких,
# что (n / m) = (p / q) и дробь (p / q) — несократимая.
x, y = int(input()), int(input())
print(*reduce_fraction(x, y))

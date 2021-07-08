def gcd(a, b):
    if not (a != 0 and b != 0):
        return a + b
    if a > b:
        a = a % b
    else:
        b = b % a
    return gcd(a, b)


# Для быстрого вычисления наибольшего общего делителя двух чисел используют алгоритм Евклида.
# Он построен на следующем соотношении: НОД(a,b)=НОД(b,a % b).
x, y = int(input()), int(input())
print(gcd(x, y))

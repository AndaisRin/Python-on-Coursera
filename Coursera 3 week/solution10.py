#Даны действительные коэффициенты a, b, c, при этом a != 0.
# Решите квадратное уравнение ax²+bx+c=0 и выведите все его корни.

a, b, c = float(input()), float(input()), float(input())
d = b ** 2 - 4 * a * c
d1, d2 = None, None
if d < 0:
    print()
elif d == 0:
    print(-b / (2 * a))
else:
    d1 = (-b - d ** 0.5) / (2 * a)
    d2 = (-b + d ** 0.5) / (2 * a)
    if d1 > d2:
        d1, d2 = d2, d1
    print(d1, d2)

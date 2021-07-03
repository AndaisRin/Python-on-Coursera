#Даны вещественные числа a, b, c, d, e, f. Известно, что система линейных уравнений:
#ax + by = e
#cx + dy = f
#имеет ровно одно решение. Выведите два числа x и y, являющиеся решением этой системы.

a, b, c = float(input()), float(input()), float(input())
d, e, f = float(input()), float(input()), float(input())
D = a * d - b * c
x = (e * d - b * f) / D
y = (a * f - e * c) / D
print(x, y)

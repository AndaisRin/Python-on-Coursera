def distance(a1, b1, a2, b2):
    return ((a2 - a1) ** 2 + (b2 - b1) ** 2) ** 0.5


#Напишите функцию, вычисляющую длину отрезка по координатам его концов.
# С помощью этой функции напишите программу, вычисляющую периметр треугольника по координатам трех его вершин.
x1, y1, x2, y2, x3, y3 = float(input()), float(input()), float(input()), float(
    input()), float(input()), float(input())
perimeter = distance(x1, y1, x2, y2) + distance(x2, y2, x3, y3)
perimeter += distance(x1, y1, x3, y3)
print(perimeter)

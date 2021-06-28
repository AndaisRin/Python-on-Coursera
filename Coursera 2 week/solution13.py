#Даны три стороны треугольника a,b,c. Определите тип треугольника с заданными сторонами. 
#Выведите одно из четырех слов: rectangular для прямоугольного треугольника, 
#acute для остроугольного треугольника, obtuse для тупоугольного треугольника или 
#impossible, если треугольника с такими сторонами не существует (считаем, что вырожденный треугольник тоже невозможен).

a = int(input())
b = int(input())
c = int(input())
if not (a + b > c and b + c > a and a + c > b):
    print('impossible')
else:
    max1 = max(a, b, c)
    min1 = min(a, b, c)
    ost = a + b + c - max1 - min1
    if max1 ** 2 == min1 ** 2 + ost ** 2:
        print('rectangular')
    elif max1 ** 2 > min1 ** 2 + ost ** 2:
        print('obtuse')
    else:
        print('acute')

#Даны координаты двух точек на плоскости, требуется определить, 
# лежат ли они в одной координатной четверти или нет (все координаты отличны от нуля).

x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())
if x1 * x2 / abs(x1 * x2) == 1 and y1 * y2 / abs(y1 * y2) == 1:
    print('YES')
else:
    print('NO')

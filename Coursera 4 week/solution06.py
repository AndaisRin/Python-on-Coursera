def distance(a1, b1, a2, b2):
    return ((a2 - a1) ** 2 + (b2 - b1) ** 2) ** 0.5


def IsPointInCircle(x, y, xc, yc, r):
    return r >= distance(x, y, xc, yc)


# Даны пять действительных чисел: x, y, xc, yc, r.
# Проверьте, принадлежит ли точка (x,y) кругу с центром (xc, yc) и радиусом r.
# Если точка принадлежит кругу, выведите слово YES, иначе выведите слово NO.
x1, y1, xc1, yc1, r1 = float(input()), float(input()), float(input()), float(
    input()), float(input())
if IsPointInCircle(x1, y1, xc1, yc1, r1):
    print('YES')
else:
    print('NO')

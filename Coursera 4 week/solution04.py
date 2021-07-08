def IsPointInSquare(a1, b1):
    return abs(a1) <= 1 and abs(b1) <= 1


# Даны два действительных числа x и y. Проверьте, принадлежит ли точка с координатами (x,y)
# квадрату (-1,-1; -1,1; 1,-1; 1,1) (включая его границу).
# Если точка принадлежит квадрату, выведите слово YES, иначе выведите слово NO.
x1, y1 = float(input()), float(input())
if IsPointInSquare(x1, y1):
    print('YES')
else:
    print('NO')

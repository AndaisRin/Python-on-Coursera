#За многие годы заточения узник замка Иф проделал в стене прямоугольное отверстие размером D×E.
#Замок Иф сложен из кирпичей, размером A×B×C. 
#Определите, сможет ли узник выбрасывать кирпичи в море через это отверстие.

a, b, c, d, e = int(input()), int(input()), int(input()), int(input()), int(input())

if min(a, b, c) * (a + b + c - min(a, b, c) - max(a, b, c) <= d * e) and min(
        a, b, c) <= min(d, e) and (
        a + b + c - min(a, b, c) - max(a, b, c)) <= d + e - min(d, e):
    print('YES')
else:
    print('NO')

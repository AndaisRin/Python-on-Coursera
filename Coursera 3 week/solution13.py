# Даны числа a, b, c, d, e, f. Решите систему линейных уравнений
# ax + by = e
# cx + dy = f
# Если система не имеет решений, то программа должна вывести единственное число 0.
# Если система имеет бесконечно много решений, каждое из которых имеет вид y=px+q, то программа должна вывести число 1, а затем значения p и q.
# Если система имеет единственное решение (x₀,y₀), то программа должна вывести число 2, а затем значения x₀ и y₀.
# Если система имеет бесконечно много решений вида x=x₀, y — любое, то программа должна вывести число 3, а затем значение x₀.
# Если система имеет бесконечно много решений вида y=y₀, x — любое, то программа должна вывести число 4, а затем значение y₀.
# Если любая пара чисел (x,y) является решением, то программа должна вывести число 5.

a, b, c = float(input()), float(input()), float(input())
d, e, f = float(input()), float(input()), float(input())

D = a * d - b * c
Dx = e * d - b * f
Dy = a * f - e * c

if a == 0 and b == 0 and c == 0 and d == 0 and e == 0 and f == 0:
    print(5)
elif D == 0 and Dy != 0:
    print(0)
elif a == 0 and b == 0 and e != 0:
    print(0)
elif c == 0 and d == 0 and f != 0:
    print(0)
elif a == 0 and c == 0 and Dx != 0:
    print(0)
elif b == 0 and d == 0 and Dx != 0:
    print(0)
elif D == 0 and Dy == 0:
    if b == 0 and d == 0:
        if a != 0 and c != 0:
            print(3, e / a)
        elif a == 0:
            if e == 0:
                print(3, f / c)
        elif c == 0:
            if f == 0:
                print(3, e / a)
    elif a == 0 and c == 0:
        if b != 0:
            print(4, e / b)
        elif d != 0:
            print(4, f / d)
    elif b != 0:
        print(1, -a / b, e / b)
    elif d != 0:
        print(1, -c / d, f / d)
else:
    x = Dx / D
    y = Dy / D
    print(2, x, y)

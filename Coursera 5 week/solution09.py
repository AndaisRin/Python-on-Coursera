# Даны числа a, b, c, d, e. Подсчитайте количество таких целых чисел от 0 до 1000 (включительно),
# которые являются корнями уравнения (ax³+bx²+cx+d)/(x-e)=0, и выведите их количество.

a, b, c, = int(input()), int(input()), int(input())
d, e = int(input()), int(input())
i = 0
for x in range(1001):
    if x != e:
        if (a * x ** 3 + b * x ** 2 + c * x + d) / (x - e) == 0:
            i += 1
print(i)

def f_xor(a, b):
    return a != b


# Напишите функцию xor(x, y) реализующую функцию "Исключающее ИЛИ"
# двух логических переменных x и y.
x1, y1 = int(input()), int(input())
if f_xor(x1, y1):
    print(1)
else:
    print(0)

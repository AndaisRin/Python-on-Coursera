# Найдите и выведите все двузначные числа, которые равны удвоенному произведению своих цифр.

for i in range(10, 99):
    a = i // 10
    b = i % 10
    if i == 2 * a * b:
        print(i)

# Дано несколько чисел. Подсчитайте, сколько из них равны нулю, и выведите это количество.

x = int(input())
i = 0
for _ in range(x):
    n = int(input())
    if n == 0:
        i += 1
print(i)
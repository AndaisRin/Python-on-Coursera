# Для настольной игры используются карточки с номерами от 1 до N.Одна карточка потерялась.
# Найдите ее, зная номера оставшихся карточек.

n = int(input())
mas_input, mas_right = [], []
for i in range(1, n + 1):
    mas_right.append(i)
for i in range(n - 1):
    mas_input.append(int(input()))
for i in range(n):
    if mas_right[i] not in mas_input:
        print(mas_right[i])

# Даны два целых числа A и B (при этом A≤B). Выведите все числа от A до B включительно.

i, j = int(input()), int(input())
for i in range(i, j + 1):
    print(i, end=' ')

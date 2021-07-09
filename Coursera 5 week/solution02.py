# Даны два целых числа A и В. Выведите все числа от A до B включительно, в порядке
# возрастания,если A < B, или в порядке убывания в противном случае.

i, j = int(input()), int(input())
if i <= j:
    for i in range(i, j + 1):
        print(i, end=' ')
else:
    for i in range(i, j - 1, -1):
        print(i, end=' ')

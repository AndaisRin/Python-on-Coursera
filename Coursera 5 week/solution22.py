def min_num(mas):
    new_mas = []
    for i in range(len(mas)):
        if mas[i] > 0:
            new_mas.append(mas[i])
    new_mas.sort()
    print(new_mas[0])


# Выведите значение наименьшего из всех положительных элементов в списке.
# Известно, что в списке есть хотя бы один положительный элемент, а значения всех элементов списка по модулю не превосходят 1000.
s = list(map(int, input().split()))
min_num(s)

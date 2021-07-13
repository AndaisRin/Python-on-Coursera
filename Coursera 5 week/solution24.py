def revers(mas):
    new_mas = []
    for i in range(len(mas)):
        new_mas.append(mas[i])
    print(*new_mas[::-1])


# Выведите элементы данного списка в обратном порядке, не изменяя сам список.
s = list(map(int, input().split()))
revers(s)

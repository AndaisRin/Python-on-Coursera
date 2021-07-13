def min_num(mas):
    new_mas = []
    for i in range(len(mas)):
        if mas[i] % 2 != 0:
            new_mas.append(mas[i])
    new_mas.sort()
    print(new_mas[0])


#Выведите значение наименьшего нечетного элемента списка, гарантируется, что хотя бы один нечётный элемент в списке есть.
s = list(map(int, input().split()))
min_num(s)

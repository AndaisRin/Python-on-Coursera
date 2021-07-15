def intersection(a, b):
    s = []
    i, j = 0, 0
    while i < len(a) and j < len(b):
        if a[i] == b[j]:
            s.append(a[i])
            i += 1
            j += 1
        elif a[i] > b[j]:
            j += 1
        else:
            i += 1
    print(*s)


# Даны два списка, упорядоченных по возрастанию (каждый список состоит из различных элементов).
# Найдите пересечение множеств элементов этих списков, то есть те числа, которые являются элементами
# обоих списков. Алгоритм должен иметь сложность O(len(A)+len(B)).
s1 = list(map(int, input().split()))
s2 = list(map(int, input().split()))
intersection(s1, s2)

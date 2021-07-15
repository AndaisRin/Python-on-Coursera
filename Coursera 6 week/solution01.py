def merge(a, b):
    s = []
    i, j = 0, 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            s.append(a[i])
            i += 1
        else:
            s.append(b[j])
            j += 1
    s += a[i:] + b[j:]
    print(*s)


# Даны два целочисленных списка A и B, упорядоченных по неубыванию. Объедините их в один упорядоченный
# список С (то есть он должен содержать len(A)+len(B) элементов). Решение оформите в виде функции merge(A, B),
# возвращающей новый список. Алгоритм должен иметь сложность O(len(A)+len(B)).
s1 = list(map(int, input().split()))
s2 = list(map(int, input().split()))
merge(s1, s2)

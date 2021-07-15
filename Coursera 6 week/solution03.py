# Отсортируйте данный массив, используя встроенную сортировку.
n = int(input())
s1 = list(map(int, input().split()))
s1.sort()
print(*s1)

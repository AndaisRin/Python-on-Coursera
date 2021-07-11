# Найдите количество положительных элементов в данном списке.

s = list(map(int, input().split()))
a, b = 0, 0
for i in range(len(s)):
    if s[i] >= a:
        a, b = s[i], i
print(a, b)

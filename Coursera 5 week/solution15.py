# Найдите количество положительных элементов в данном списке.

a = list(map(int, input().split()))
count = 0
for i in range(len(a)):
    if a[i] > 0:
        count += 1
print(count)

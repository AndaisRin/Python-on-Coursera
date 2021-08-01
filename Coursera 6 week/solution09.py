# Сортировка подсчетом
# Дан список из N (N≤2*10⁵) элементов, которые принимают целые значения от 0 до 100 (100 включая).
# Отсортируйте этот список в порядке неубывания элементов. Выведите полученный список.

num_list = list(map(int, input().split()))
cnt = [0] * (max(num_list) + 1)
for i in range(len(num_list)):
    cnt[num_list[i]] += 1
pos = 0
for num in range(len(cnt)):
    for i in range(cnt[num]):
        num_list[pos] = num
        pos += 1
print(*num_list)

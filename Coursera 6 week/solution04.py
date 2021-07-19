# В обувном магазине продается обувь разного размера. Известно, что одну пару обуви можно надеть на другую,
# если она хотя бы на три размера больше. В магазин пришел покупатель.Требуется определить, какое наибольшее
# количество пар обуви сможет предложить ему продавец так, чтобы он смог надеть их все одновременно.

start_size = int(input())
a = sorted(set(list(map(int, input().split()))))
count_par = 0
shoes_size = 0
for i in range(len(a)):
    if a[i] < start_size:
        continue
    elif a[i] == shoes_size:
        continue
    elif a[i] == start_size:
        count_par += 1
        shoes_size = a[i]
    elif a[i] - shoes_size >= 3:
        count_par += 1
        shoes_size = a[i]
print(count_par)

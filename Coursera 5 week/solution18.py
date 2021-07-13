def is_ascending(mas):
    j = 1
    for i in range(1, len(mas)):
        if mas[i] > mas[i - 1]:
            j += 1
    return print('YES') if j == len(mas) else print('NO')


# Дан список. Определите, является ли он монотонно возрастающим.
# Выведите YES, если массив монотонно возрастает и NO в противном случае.
s = list(map(int, input().split()))
is_ascending(s)

def sum_pos():
    n = int(input())
    if n != 0:
        return n + sum_pos()
    return n


# Дана последовательность чисел, завершающаяся числом 0.
# Найдите сумму всех этих чисел, не используя цикл.
print(sum_pos())

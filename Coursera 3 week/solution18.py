# Дана строка. Найдите в этой строке второе вхождение буквы f и выведите индекс этого вхождения.
# Если буква f в данной строке встречается только один раз, выведите число -1,
# а если не встречается ни разу, выведите число -2. При решении этой задачи нельзя использовать метод count.

string = input()
substring = "f"
pos = string.find(substring)
if pos == -1:
    print(-2)
else:
    alt_pos = string.find(substring, pos + 1)
    if alt_pos == pos:
        print(-1)
    else:
        print(alt_pos)

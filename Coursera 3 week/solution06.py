#Процентная ставка по вкладу составляет P процентов годовых, которые прибавляются к сумме вклада.
# Вклад составляет X рублей Y копеек. Определите размер вклада через год.
# При решении этой задачи нельзя пользоваться условными инструкциями и циклами.

p, x, y = int(input()), int(input()), int(input())
d = x * 100 + y
d = int(d * (100 + p) / 100)
x = d // 100
y = d % 100
print(x, y)
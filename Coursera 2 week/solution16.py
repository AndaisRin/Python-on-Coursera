#Даны три целых числа. Определите, сколько среди них совпадающих. 
#Программа должна вывести одно из чисел: 
# 3 (если все совпадают), 2 (если два совпадает) или 0 (если все числа различны).

a, b, c = int(input()), int(input()), int(input())

if a == b == c:
    print(3)
elif a == b or a == c or b == c:
    print(2)
else:
    print(0)

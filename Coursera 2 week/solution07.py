#Заданы две клетки шахматной доски. 
#Если они покрашены в один цвет, то выведите слово YES, а если в разные цвета – то NO.

num11 = int(input())
num12 = int(input())
num21 = int(input())
num22 = int(input())
if (abs(num11 - num12)) % 2 == (abs(num21 - num22)) % 2:
    print('YES')
else:
    print('NO')

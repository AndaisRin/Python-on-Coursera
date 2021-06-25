#Дано целое число N. Выведите следующее за ним четное число.

count = int(input())
if count % 2 == 0:
    print(count + 2)
else:
    print(count + 1)

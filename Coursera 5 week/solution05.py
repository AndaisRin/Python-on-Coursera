# Напишите программу, которая по данному числу n от 1 до 9 выводит на экран n флагов.
# Внутри каждого флага должен быть записан его номер — число от 1 до n.

x = int(input())
for i in range(x):
    print('+___ ', end='')
print()
for i in range(x):
    print('|', i + 1, ' / ', sep='', end='')
print()
for i in range(x):
    print('|__\ ', end='')
print()
for i in range(x):
    print('|    ', end='')

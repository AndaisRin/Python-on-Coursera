#По данному целому числу N распечатайте все квадраты натуральных чисел,
# не превосходящие N, в порядке возрастания.

a = int(input())
b = a ** 0.5
b = int(b // 1)
n = 1
while n <= b:
    print(n ** 2, end=' ')
    n = n + 1

#Напишите программу, которая находит в массиве элемент, самый близкий по величине к  данному числу.

n = int(input())
s = list(map(int, input().split()))
x = int(input())
print(min(s, key=lambda a: abs(a - x)))

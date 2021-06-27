a = int(input())
b = int(input())
n = a
i = 1
while b > n:
    n = n + n * 0.1
    i = i + 1
print(i)

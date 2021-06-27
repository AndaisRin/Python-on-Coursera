a = 0
b = 1
c = a
while b != a:
    b = int(input())
    if b > c:
        c = b
print(c)

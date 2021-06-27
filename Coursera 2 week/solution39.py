a = 0
i = 0
b = -1
while 1 != 0:
    b = int(input())
    if b == 0:
        break
    if b > a:
        a, i = b, 1
    elif b == a:
        i += 1
print(i)

a = -1
i = -1
b = 0
while 1 != 0:
    b = a
    a = int(input())
    if a == 0:
        break
    if b < a:
        i = i + 1
print(i)

a, b, i, i1 = -1, 0, 1, -1
while 1 != 0:
    b = a
    a = int(input())
    if a == 0:
        i1 = max(i, i1)
        break
    if b == a:
        i = i + 1
    if b != a:
        i1 = max(i, i1)
        i = 1
print(i1)

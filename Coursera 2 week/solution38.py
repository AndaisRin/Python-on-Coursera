a = int(input())
b = int(input())
c = b
while 1 != 0:
    if b >= a:
        c, a = a, b
    elif c < b <= a:
        c = b
    b = int(input())
    if b == 0:
        break
print(c)

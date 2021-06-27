a = int(input())
b = int(input())
c = int(input())
if not (a + b > c and b + c > a and a + c > b):
    print('impossible')
else:
    max1 = max(a, b, c)
    min1 = min(a, b, c)
    ost = a + b + c - max1 - min1
    if max1 ** 2 == min1 ** 2 + ost ** 2:
        print('rectangular')
    elif max1 ** 2 > min1 ** 2 + ost ** 2:
        print('obtuse')
    else:
        print('acute')

num11 = int(input())
num12 = int(input())
num21 = int(input())
num22 = int(input())
if (abs(num11 - num21) <= 1) and (abs(num12 - num22) <= 1):
    print('YES')
else:
    print('NO')

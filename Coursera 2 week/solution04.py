chis1 = int(input())
if (chis1 % 4 == 0 and chis1 % 100 != 0) or chis1 % 400 == 0:
    print('YES')
else:
    print('NO')

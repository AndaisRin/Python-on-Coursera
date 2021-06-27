num1 = int(input())
num2 = int(input())
num3 = int(input())
if (num3 % num1 == 0 or num3 % num2 == 0) and \
        (num3 >= num1 or num3 >= num2) and num3 <= num1 * num2:
    print('YES')
else:
    print('NO')

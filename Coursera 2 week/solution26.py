a = int(input())
b = 2
while a >= b:
    if a % b == 0:
        print(b)
        break
    b = b + 1

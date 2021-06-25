#Дано трехзначное число. Найдите сумму его цифр.

count = int(input())
a = count // 100
b = (count % 100) // 10
c = count % 10
print(a + b + c)

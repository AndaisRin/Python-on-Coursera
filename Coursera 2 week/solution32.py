#По данному натуральному n вычислите сумму 1²+2²+3²+...+n².

n = int(input())
sum = 0
i = 0
while i <= n:
    sum = sum + i ** 2
    i = i + 1
print(sum)

# По данному натуральном n вычислите сумму 1²+2²+3²+...+n².
def sum_sqr(n):
    if n > 0:
        n = n ** 2 + sum_sqr(n - 1)
    return n


x = int(input())
print(sum_sqr(x))

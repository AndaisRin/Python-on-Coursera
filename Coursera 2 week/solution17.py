a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
if min(a, b, c) * (a + b + c - min(a, b, c) - max(a, b, c) <= d * e) and min(
        a, b, c) <= min(d, e) and (
        a + b + c - min(a, b, c) - max(a, b, c)) <= d + e - min(d, e):
    print('YES')
else:
    print('NO')

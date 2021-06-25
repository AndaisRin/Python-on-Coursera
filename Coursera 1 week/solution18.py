v = int(input())
t = int(input())
if v > 0:
    print((abs(t * v)) % 109)
else:
    print(abs(abs(t * v) % -109))

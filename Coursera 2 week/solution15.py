a = int(input())
b = int(input())
c = int(input())
print(min(a, b, c), a + b + c - max(a, b, c) - min(a, b, c), max(a, b, c))

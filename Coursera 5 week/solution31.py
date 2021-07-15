# Переставьте соседние элементы списка (A[0] c A[1],A[2] c A[3] и т.д.).
# Если элементов нечетное число, то последний элемент остается на своем месте.

s = list(map(int, input().split()))
s1 = []
for i in range(0, len(s) - 1, 2):
    s1.append(s[i + 1])
    s1.append(s[i])
if len(s) != len(s1):
    s1.append(s[len(s) - 1])
print(*s1)

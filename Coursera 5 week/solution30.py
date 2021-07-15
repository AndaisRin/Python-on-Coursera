# Дан список, упорядоченный по неубыванию элементов в нем.
# Определите, сколько в нем различных элементов.

s = list(map(int, input().split()))
s1 = []
for j in range(len(s)):
    if s[j] not in s1:
        s1.append(s[j])
print(len(s1))

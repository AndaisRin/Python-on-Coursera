# Петя перешёл в другую школу. На уроке физкультуры ему понадобилось определить своё место в строю. Помогите ему это сделать.

s = list(map(int, input().split()))
x = int(input())
i = 1
for j in range(len(s)):
    if s[j] >= x:
        i += 1
print(i)

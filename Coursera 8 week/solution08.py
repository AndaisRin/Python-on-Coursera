# По заданному на входе числу 0≤n≤2000 выведите последовательность факториалов: 0!,1!,2!,…,n!
from math import factorial

print(*map(lambda x: factorial(x), range(int(input()) + 1)))

# По заданной последовательности: (a₁,…,an) посчитайте последовательность частичных сумм: (S₁,…,Sn), где Sk=a₁+a₂+…+ak.
from itertools import accumulate

print(*accumulate(map(int, input().split())))

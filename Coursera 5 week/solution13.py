# Выведите все элементы списка с четными индексами (то есть A[0], A[2], A[4], ...). 

a = list(map(int, input().split()))
for i in range(0, len(a), 2):
    print(a[i], end=' ')

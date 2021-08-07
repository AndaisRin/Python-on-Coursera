# Такси
# В первой строке записаны N чисел через пробел, задающих расстояния в километрах от работы до домов
# сотрудников компании. Во второй строке записаны N чисел — тарифы за проезд одного километра в такси.
# Выведите одно целое число — наименьшую сумму, которую придется заплатить за доставку всех сотрудников.

data = open('input.txt', 'r', encoding='utf-8')
distance = data.readline().split()
distance = list(int(x) for x in distance)
distance.sort()
price = data.readline().split()
price = list(int(x) for x in price)
price.sort(reverse=True)
summa = 0
for i in range(len(distance)):
    summa += (distance[i] * price[i])
print(summa)

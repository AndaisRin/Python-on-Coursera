#Даны три целых числа. Найдите наибольшее из них (программа должна вывести ровно одно целое число).
#Какое наименьшее число операторов сравнения (>, <, >=, <=) необходимо для решения этой задачи?

chis1, chis2, chis3, = int(input()), int(input()), int(input())

if chis1>chis2:
    max_chis1=chis1
else:
    max_chis1=chis2
if chis2>chis3:
    max_chis2=chis2
else:
    max_chis2=chis3
if max_chis1>max_chis2:
    print(max_chis1)
else:
    print(max_chis2)

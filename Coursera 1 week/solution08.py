#Дано натуральное число. Найдите цифру, стоящую в разряде десятков в его десятичной записи 
#(вторую справа цифру или 0, если число меньше 10). 

count = int(input())
print((count % 100) // 10)

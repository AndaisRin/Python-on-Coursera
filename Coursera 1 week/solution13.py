#Напишите программу, которая считывает целое число и выводит текст, аналогичный приведенному в примере. 
#Нельзя пользоваться конкатенацией строк, используйте print с несколькими параметрами.

count = int(input())
print('The next number for the number ', count, sep='', end='')
print(' is ', count + 1, '.', sep='')
print('The previous number for the number ', count, sep='', end='')
print(' is ', count - 1, '.', sep='')

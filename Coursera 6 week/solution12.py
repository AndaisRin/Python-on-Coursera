# Программа получает на вход число участников олимпиады N. Далее идет N строк, в каждой
# строке записана фамилия участника, затем, через пробел, набранное им количество баллов.
# Выведите список участников (только фамилии) в порядке убывания набранных баллов.
n = int(input())
students_list = []
for i in range(n):
    students_list.append(input().strip().split())
students_list.sort(key=lambda x: int(x[1]), reverse=True)
for i in range(n):
    print(students_list[i][0])

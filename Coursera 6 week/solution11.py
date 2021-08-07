# Определите и выведите максимальные баллы участников олимпиады в 9, 10 и 11 классах.
# Информация о результатах олимпиады записана в файле, каждая строка которого имеет вид:
# фамилия имя класс балл
# Иванов Сергей 9 90
#
# Выведите три числа: максимальные баллы по 9 классу, по 10 классу, по 11 классу.
# Входной файл в кодировке utf-8 (используйте open('input.txt', 'r', encoding='utf-8')).


class Students:
    class_no = 0
    score = 0


def max_score(no_class, my_list):
    max_s = 0
    for i in range(len(my_list)):
        if no_class == my_list[i].class_no and my_list[i].score > max_s:
            max_s = my_list[i].score
    return max_s


data = open('input.txt', 'r', encoding='utf-8')
peopleList = []
lines = data.readlines()
for line in lines:
    tempStudentsData = line.split()
    student = Students()
    student.class_no = int(tempStudentsData[2])
    student.score = int(tempStudentsData[3])
    peopleList.append(student)

print(max_score(9, peopleList), end=' ')
print(max_score(10, peopleList), end=' ')
print(max_score(11, peopleList))

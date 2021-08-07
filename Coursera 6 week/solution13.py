# Определите количество школьников, ставших победителями в каждом классе.
# Информация о результатах олимпиады записана в файле, каждая строка которого имеет вид:
# фамилия имя класс балл
# Иванов Сергей 9 90
#
# Выведите три числа: количество победителей олимпиады по 9 классу, по 10 классу, по 11 классу.
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


def count_max(no_class, my_list):
    max_c = max_score(no_class, my_list)
    student_count = 0
    for i in range(len(my_list)):
        if no_class == my_list[i].class_no and max_c == my_list[i].score:
            student_count += 1
    return student_count


data = open('input.txt', 'r', encoding='utf-8')
peopleList = []
lines = data.readlines()
for line in lines:
    tempStudentsData = line.split()
    student = Students()
    student.class_no = int(tempStudentsData[2])
    student.score = int(tempStudentsData[3])
    peopleList.append(student)

print(count_max(9, peopleList), end=' ')
print(count_max(10, peopleList), end=' ')
print(count_max(11, peopleList))

# Определите и выведите средние баллы участников олимпиады в 9 классе, в 10 классе, в 11 классе.
# Информация о результатах олимпиады записана в файле, каждая строка которого имеет вид: 
# фамилия имя класс балл
# Иванов Сергей 9 90
# 
# Выведите три числа: средние баллы по 9 классу, по 10 классу, по 11 классу. 
# Входной файл в кодировке utf-8 (используйте open('input.txt', 'r', encoding='utf-8')).

class Students:
    surname = ''
    name = ''
    class_no = 0
    score = 0


def mean_score(no_class, my_list):
    sum_score, j = 0, 0
    for i in range(len(my_list)):
        if no_class == my_list[i].class_no:
            sum_score += my_list[i].score
            j += 1
    if j == 0:
        return 0
    else:
        return sum_score / j


data = open('input.txt', 'r', encoding='utf-8')
peopleList = []
lines = data.readlines()
for line in lines:
    tempStudentsData = line.split()
    student = Students()
    student.surname = tempStudentsData[0]
    student.name = tempStudentsData[1]
    student.class_no = int(tempStudentsData[2])
    student.score = int(tempStudentsData[3])
    peopleList.append(student)

print(mean_score(9, peopleList), end=' ')
print(mean_score(10, peopleList), end=' ')
print(mean_score(11, peopleList))

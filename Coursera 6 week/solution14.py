# Проходной балл
# Программа должна вывести проходной балл в конкурсе. Выведенное значение должно быть минимальным баллом, который набрал абитуриент, прошедший по конкурсу.
# Также возможны две ситуации, когда проходной балл не определен.
# Если будут зачислены все абитуриенты, не имеющие неудовлетворительных оценок, программа должна вывести число 0.
# Если количество имеющих равный максимальный балл абитуриентов больше чем K, программа должна вывести число 1.
def min_score(seats, students_list):
    if seats >= len(students_list):
        return 0
    elif students_list[0] == students_list[seats]:
        return 1
    for i in range(k, 0, -1):
        if students_list[i] < students_list[i - 1]:
            return students_list[i - 1]


data = open('input.txt', 'r', encoding='utf-8')
k = int(data.readline())
people_list = []
for line in data:
    first, second, third = [int(i) for i in line.split()[-3:]]
    if first >= 40 and second >= 40 and third >= 40:
        people_list.append(first + second + third)
people_list.sort(reverse=True)
print(min_score(k, people_list))

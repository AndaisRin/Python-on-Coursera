# Определите школы, из которых в олимпиаде принимало участие больше всего участников.
# В этой задаче необходимо считывать данные построчно, не сохраняя в памяти данные обо
# всех участниках, а только подсчитывая число участников для каждой школы.
# Информация о результатах олимпиады записана в файле, каждая из строк которого имеет вид:
# фамилия имя школа балл
# Выведите номера этих школ в порядке возрастания.

data = open('input.txt', 'r', encoding='utf-8')
count_school = {}
for line in data:
    school, score = list(map(int, line.split()[-2:]))
    school = int(school)
    if school not in count_school.keys():
        count_school[school] = 1
    else:
        count_school[school] += 1
max_count = max(count_school.values())
max_school = []
for key, value in count_school.items():
    if value == max_count:
        max_school.append(key)
max_school.sort()
print(*max_school)

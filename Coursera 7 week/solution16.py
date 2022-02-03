# Каждая строка входного файла содержит фамилию кандидата, за которого отдают голоса
# выборщики этого штата, затем через пробел идет количество выборщиков,отдавших голоса за
# этого кандидата. Выведите фамилии всех кандидатов в лексикографическом порядке,
# затем, через пробел, количество отданных за них голосов.
votes = dict()
data = open('input.txt', 'r', encoding='utf8')
for line in data:
    vote = line.split()
    votes[vote[0]] = votes.get(vote[0], 0) + int(vote[1])
for name, val in sorted(votes.items()):
    print(name, val)
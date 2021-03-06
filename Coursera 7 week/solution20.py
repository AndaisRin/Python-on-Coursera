# Статья 83 закона “О выборах депутатов Государственной Думы Федерального Собрания
# Российской Федерации” определяет следующий алгоритм пропорционального распределения мест
# в парламенте. Необходимо распределить 450 мест между партиями, участвовавших в выборах.
# Сначала подсчитывается сумма голосов избирателей, поданных за каждую партию и
# подсчитывается сумма голосов, поданных за все партии. Эта сумма делится на 450,
# получается величина, называемая “первое избирательное частное” (смысл первого
# избирательного частного - это количество голосов избирателей, которое необходимо набрать
# для получения одного места в парламенте). Далее каждая партия получает столько мест в
# парламенте, чему равна целая часть от деления числа голосов за данную партию на первое
# избирательное частное.Если после первого раунда распределения мест сумма количества мест,
# отданных партиям, меньше 450, то оставшиеся места передаются по одному партиям, в
# порядке убывания дробной части частного от деления числа голосов за данную партию на
# первое избирательное частное. Если же для двух партий эти дробные части равны, то
# преимущество отдается той партии, которая получила большее число голосов.
# Формат ввода
# На вход программе подается список партий, участвовавших в выборах. Каждая строка
# входного файла содержит название партии (строка, возможно, содержащая пробелы), затем,
# через пробел, количество голосов, полученных данной партией – число, не превосходящее 10⁸.
# Формат вывода
# Программа должна вывести названия всех партий и количество голосов в парламенте,
# полученных данной партией. Названия необходимо выводить в том же порядке, в котором они шли во входных данных.

names, votes = list(), list()
sumVotes = 0
data = open('input.txt')
for line in data:
    line = line.split()
    partyName = ' '.join(line[:-1])
    partyVotes = int(line[-1])
    names.append(partyName)
    votes.append(partyVotes)
    sumVotes += partyVotes
mandates, patry_part = list(), list()
sum_mandates = 0
for i in range(len(names)):
    partyMandates = (votes[i] * 450) / sumVotes
    sum_mandates += int(partyMandates)
    mandates.append(int(partyMandates))
    patry_part.append(partyMandates - int(partyMandates))
while sum_mandates < 450:
    i = 0
    for j in range(1, len(patry_part)):
        if ((patry_part[j] > patry_part[i]) or (
                patry_part[j] == patry_part[i] and votes[j] > votes[i])):
            i = j
    mandates[i] += 1
    sum_mandates += 1
    patry_part[i] = 0
for k in range(len(names)):
    print(names[k], mandates[k])

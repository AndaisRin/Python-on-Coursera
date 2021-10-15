# В выборах Президента Российской Федерации побеждает кандидат, набравший свыше половины
# числа голосов избирателей. Если такого кандидата нет, то во второй тур выборов выходят
# два кандидата, набравших наибольшее число голосов.
# Формат ввода
# Каждая строка входного файла содержит имя кандидата, за которого отдал голос один
# избиратель. Известно, что общее число кандидатов не превосходит 20, но в отличии от
# предыдущих задач список кандидатов явно не задан. Читайте данные из файла input.txt с указанием кодировки utf8.
# Формат вывода
# Если есть кандидат, набравший более 50% голосов, программа должна вывести его имя.
# Если такого кандидата нет, программа должна вывести имя кандидата, занявшего первое место,
# затем имя кандидата, занявшего второе место. Выводите данные в файл output.txt с указанием кодировки utf8.

names = dict()
sum_votes = 0
data = open('input.txt', 'r', encoding='utf8')
out_data = open('output.txt', 'w', encoding='utf8')
for line in data:
    string = line.strip()
    if string not in names:
        names[string] = 1
    else:
        names[string] = names[string] + 1
    sum_votes += 1
list_words = list(names.items())
list_words.sort(key=lambda x: -x[1])
if list_words[0][1] / sum_votes > 0.5:
    print(list_words[0][0], file=out_data)
else:
    print(list_words[0][0], sep="\n", file=out_data)
    print(list_words[1][0], sep="\n", file=out_data)
data.close()
out_data.close()

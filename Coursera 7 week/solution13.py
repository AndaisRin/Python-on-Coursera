# Программа получает на вход количество стран N. Далее идет N строк, каждая строка
# начинается с названия страны, затем идут названия городов этой страны. Название каждого
# город состоит из одного слова. В следующей строке записано число M,
# далее идут M запросов — названия каких-то M городов, перечисленных выше.

def create_dict():
    global synonym_dict
    s = list(map(str, input().split()))
    for j in range(1, len(s)):
        city_county[s[j]] = s[0]


synonym_dict = dict()
n = int(input())
for i in range(n):
    create_dict()
m = int(input())
for i in range(m):
    print(synonym_dict[input()])

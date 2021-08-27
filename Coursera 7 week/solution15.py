# Программа получает на вход количество пар синонимов N. Далее следует N строк, каждая
# строка содержит ровно два слова-синонима. После этого следует одно слово.
# Программа должна вывести синоним к данному слову.
def create_dict():
    global synonym_dict
    s = list(map(str, input().split()))
    synonym_dict[s[0]] = s[1]


synonym_dict = dict()
n = int(input())
for i in range(n):
    create_dict()
k = input()
for keys, items in synonym_dict.items():
    if k in keys:
        print(items)
    elif k in items:
        print(keys)

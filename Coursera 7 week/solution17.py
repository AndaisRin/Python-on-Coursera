# Дан текст. Выведите слово, которое в этом тексте встречается чаще всего. 
# Если таких слов несколько, выведите то, которое меньше в лексикографическом порядке.
count_words = dict()
data = open('input.txt', 'r', encoding='utf8')
for line in data:
    words = list(map(str, line.split()))
    for i in range(len(words)):
        if words[i] not in count_words.keys():
            count_words[words[i]] = 1
        else:
            count_words[words[i]] += 1
max_count = max(count_words.values())
max_word = []
for key, value in count_words.items():
    if value == max_count:
        max_word.append(key)
max_word.sort()
print(max_word[0])

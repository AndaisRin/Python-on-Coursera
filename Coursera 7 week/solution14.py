# Во входном файле (вы можете читать данные из файла input.txt) записан текст.
# Словом считается последовательность непробельных подряд идущих символов. Слова разделены
# одним или большим числом пробелов или символами конца строки. Для каждого слова из этого
# текста подсчитайте, сколько раз оно встречалось в этом тексте ранее.
# Входные данные:
# one two one tho three
# Вывод программы:
# 0 0 1 0 0


data = open('input.txt', 'r', encoding='utf-8')
count_words = {}
for line in data:
    for word in line.split():
        if word not in count_words.keys():
            count_words[word] = 0
            print(count_words[word], end=' ')
        else:
            count_words[word] += 1
            print(count_words[word], end=' ')

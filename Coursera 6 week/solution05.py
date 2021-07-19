# Программа получает на вход в одной строке число S – размер свободного места на диске (натуральное, не превышает 10000),
# и число N – количество пользователей (натуральное, не превышает 100), после этого идет N чисел -
# объем данных каждого пользователя (натуральное, не превышает 1000), записанных каждое в отдельной строке.
# Выведите наибольшее количество пользователей, чьи данные могут быть помешены в архив.

n = list(map(int, input().split()))
free_size, count_users = n[0], n[1]
users_data = []
for i in range(count_users):
    users_data.append(int(input()))
users_data.sort()
data_size, i = 0, 0
for j in range(count_users):
    if data_size + users_data[j] <= free_size:
        data_size += users_data[j]
        i += 1
print(i)

# Необходимо для каждого селения определить ближайшее к нему бомбоубежище.
# В первой строке вводится число n - количество селений (1 <= n <= 100000).
# Вторая строка содержит n различных целых чисел, i-е из этих чисел задает расстояние от начала дороги до i-го селения.
# В третьей строке входных данных задается число m - количество бомбоубежищ (1 <= m <= 100000).
# Четвертая строка содержит m различных целых чисел, i-е из этих чисел задает расстояние от начала дороги до i-го бомбоубежища.

def get_input():
    num = int(input())
    lst = list(map(int, input().split()))
    num_lst = [i for i in range(1, num + 1)]
    list_all = [list(x) for x in zip(lst, num_lst)]
    return list_all


def bin_search(town, save_place):
    left = 0
    right = len(save_place) - 1
    while right - left > 1:
        middle = (right + left) // 2
        if town > save_place[middle][0]:
            left = middle
        else:
            right = middle
    save_idx = right if town > (save_place[left][0] + save_place[right][0]) // 2 else left
    return save_place[save_idx][1]


list_city = get_input()
list_safe = get_input()
list_safe.sort(key=lambda x: x[0])

for city in list_city:
    safe_num = bin_search(city[0], list_safe)
    city.append(safe_num)

list_city.sort(key=lambda x: x[1])
for i in range(len(list_city)):
    print(list_city[i][2], end=' ')

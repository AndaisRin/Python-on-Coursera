# Август и Беатриса играют в игру. Август загадал натуральное число от 1 до n.
# Беатриса пытается угадать это число, для этого она называет некоторые множества натуральных чисел.
# Август отвечает Беатрисе YES, если среди названных ею чисел есть задуманное или NO в противном случае.
# После нескольких заданных вопросов Беатриса запуталась в том, какие вопросы она задавала и какие
# ответы получила и просит вас помочь ей определить, какие числа мог задумать Август.
n = int(input())
all_possible = set(range(1, n + 1))
beatrice = input().split()
while beatrice[0] != 'HELP':
    beatrice = set(map(int, beatrice))
    august = input().split()
    if august[0] == 'YES':
        all_possible &= beatrice
    elif august[0] == 'NO':
        all_possible -= beatrice
    beatrice = input().split()
print(*sorted(all_possible))

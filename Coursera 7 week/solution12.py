# В первой строке входных данных записан номер телефона, который Вася хочет добавить в адресную книгу своего телефона.
# В следующих трех строках записаны три номера телефонов, которые уже находятся в адресной книге телефона Васи. Гарантируется,
# что каждая из записей соответствует одному из трех приведенных в условии форматов.
# Телефонные номера в адресной книге мобильного телефона имеют один из следующих форматов:
# +7<код><номер>/ 8<код><номер>/ <номер>
# где <номер> — это семь цифр, а <код> — это три цифры или три цифры в круглых скобках. Если код не указан,
# то считается, что он равен 495. Кроме того, в записи телефонного номера может стоять знак “-” между любыми двумя цифрами.
import re


def right_num():
    number = re.sub(r'\D', '', input())
    if len(number) == 7:
        number = '495' + number
    elif len(number) == 11:
        number = number[-10:]
    return number


new_num = right_num()
for i in range(3):
    print('YES') if new_num == right_num() else print('NO')

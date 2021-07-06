# Дана строка. Замените в этой строке все появления
# буквы h на букву H, кроме первого и последнего вхождения.

string = input()
pos_first = string.find('h')
pos_last = string.rfind('h')
substring = string[pos_first + 1:pos_last].replace('h', 'H')
string_first = string[:pos_first + 1]
string_last = string[pos_last:]
print(string_first + substring + string_last)

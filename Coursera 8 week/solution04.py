# Проверьте, есть ли среди данных N чисел нули.
import sys

print(any(map(lambda x: int(x) == 0, sys.stdin.read().split())))

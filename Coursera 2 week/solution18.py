#Есть две коробки, первая размером A₁×B₁×C₁, вторая размером A₂×B₂×C₂. Определите, можно ли разместить одну из
# этих коробок внутри другой, при условии, что поворачивать коробки можно только на 90 градусов вокруг ребер.
#Boxes are equal, если коробки одинаковые,
#The first box is smaller than the second one, если первая коробка может быть положена во вторую,
#The first box is larger than the second one, если вторая коробка может быть положена в первую,
#Boxes are incomparable, во всех остальных случаях.

a1, b1, c1 = int(input()), int(input()), int(input())
a2, b2, c2 = int(input()), int(input()), int(input())

min1 = min(a1, b1, c1)
max1 = max(a1, b1, c1)
ost1 = a1 + b1 + c1 - max1 - min1
min2 = min(a2, b2, c2)
max2 = max(a2, b2, c2)
ost2 = a2 + b2 + c2 - max2 - min2
if min1 == min2 and max1 == max2 and ost1 == ost2:
    print('Boxes are equal')
elif min1 <= min2 and max1 <= max2 and ost1 <= ost2:
    print('The first box is smaller than the second one')
elif min1 >= min2 and max1 >= max2 and ost1 >= ost2:
    print('The first box is larger than the second one')
else:
    print('Boxes are incomparable')

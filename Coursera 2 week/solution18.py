a1 = int(input())
b1 = int(input())
c1 = int(input())
a2 = int(input())
b2 = int(input())
c2 = int(input())
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

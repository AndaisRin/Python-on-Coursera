#Пирожок в столовой стоит A рублей и B копеек. 
#Определите, сколько рублей и копеек нужно заплатить за N пирожков.

rub = int(input())
kop = int(input())
count = int(input())
print(rub * count + (kop * count // 100), kop * count % 100)

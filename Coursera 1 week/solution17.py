#Длина Московской кольцевой автомобильной дороги —  109 километров. 
#Байкер Вася стартует с нулевого километра МКАД и едет со скоростью v километров в час. 
#На какой отметке он остановится через t часов?

v = int(input())
t = int(input())
if v > 0:
    print((abs(t * v)) % 109)
else:
    print(abs(abs(t * v) % -109))

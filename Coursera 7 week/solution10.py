# На Новом проспекте для разгрузки было решено пустить два новых автобусных маршрута на
# разных участках проспекта.  Известны конечные остановки каждого из автобусов. Определите
# количество остановок, на  которых можно пересесть с одного автобуса на другой.
stop_list = list(map(int, input().split()))
f_bus = sorted([stop_list[0], stop_list[1]])
s_bus = sorted([stop_list[2], stop_list[3]])
f_bus_stop = set(range(f_bus[0], f_bus[1] + 1))
s_bus_stop = set(range(s_bus[0], s_bus[1] + 1))
print(len(f_bus_stop.intersection(s_bus_stop)))

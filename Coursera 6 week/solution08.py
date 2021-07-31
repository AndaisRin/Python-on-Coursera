# Отсортировать список участников по алфавиту
# Известно, что фамилии всех участников — различны.
# При выводе указываете фамилию, имя участника и его балл. 

data = open('input.txt', 'r', encoding='utf-8')
peopleList = []
lines = data.readlines()
for line in lines:
    tempStudentsData = line.strip().split()
    peopleList.append(tempStudentsData)
peopleList.sort(key=lambda x: x[0])
for i in range(len(peopleList)):
    print(peopleList[i][0], peopleList[i][1], peopleList[i][3])

listOfGrades = list()  # зачетка

with open('student_info.txt', encoding='UTF-8') as f:
    infoFromFile = f.readlines()  # считываем файл в зачетку

for i in range(0, len(infoFromFile)):
    listOfGrades.append(infoFromFile[i].rstrip().split(','))

for i in range(0, len(listOfGrades)):
    listOfGrades[i][0] = list(listOfGrades[i][0])

for i in range(0, len(listOfGrades)):  # приводим к соответствующим типам
    listOfGrades[i][0][0] = int(listOfGrades[i][0][0])
    listOfGrades[i][0][1] = int(listOfGrades[i][0][1])
    listOfGrades[i][0][2] = int(listOfGrades[i][0][2])
    listOfGrades[i][5] = int(listOfGrades[i][5])
    listOfGrades[i][7] = bool(listOfGrades[i][7])

for i in range(0, len(listOfGrades)):
    listOfGrades[i][0] = tuple(listOfGrades[i][0])

for i in range(0, len(listOfGrades)):
    grade1 = listOfGrades[i][3]
    listOfGrades[i][3] = list()
    listOfGrades[i][3].append(grade1)
    listOfGrades[i][3].append(listOfGrades[i][4])
    listOfGrades[i][3].append(listOfGrades[i][5])
    del (listOfGrades[i][4])
    del (listOfGrades[i][4])


gradesETCS = []  # массив оценок студента в системе ETCS
for i in range(0, len(listOfGrades)):
    a = listOfGrades[i][0][0]
    if a == 2 or a == 4:  # оценки студента за второй курс
        gradesETCS.append(listOfGrades[i][3][1])

print(gradesETCS)

gradeSet = set(gradesETCS)  # массив приводим в множество (уникальные объекты)

less_common = None  # наиболее часто встречаемое значение
qty_less_common = len(listOfGrades)  # его количество

for item in gradeSet:
    qty = gradesETCS.count(item)  # переменной qty присваивается количество случаев item в списке gradesETCS
    if qty < qty_less_common:  # Если это количество больше максимального
        qty_less_common = qty  # то заменяем на него максимальное,
        less_common = item  # запоминаем само значение

print(less_common, ": ", qty_less_common)

dicOfGrades = {}
for i in range(0, len(listOfGrades)):
    dicOfGrades[listOfGrades[i][0]] = {
        'Subject name': listOfGrades[i][1],
        'Lecture name': listOfGrades[i][2],
        'Mark list': listOfGrades[i][3],
        'Date': listOfGrades[i][4],
        'IsSignature': listOfGrades[i][5]
    }

for i in range(0, len(listOfGrades)):
    a = listOfGrades[i][0][0]
    if a == 2 or a == 4:  # оценки студента за второй курс
        if listOfGrades[i][3][1] == less_common:
            print(listOfGrades[i][0], ":")
            print(dicOfGrades[listOfGrades[i][0]])
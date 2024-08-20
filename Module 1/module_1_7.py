#Входные данные
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

#Решение
students = sorted(students)
average_mark = []

for index_ in grades:
    count = 0
    for x in index_:
        count += x
    average_mark.append(count / len(index_))

journal = dict()
i = 0
for name in students:
    journal[name] = average_mark[i]
    i += 1

print(journal)
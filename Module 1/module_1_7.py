# Входные данные
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

# Решение
students = sorted(students)
average_mark = []

for index_ in grades:
    average_mark.append(sum(index_) / len(index_))

journal = dict()
i = 0
for name in students:
    journal[name] = average_mark[i]
    i += 1

print(journal)

my_dict = {'Alex': 43, 'Mike': 38, 'Janna': 25, 'Kris': 56}
print(f'Dict: {my_dict}')
print(f'Existing value: {my_dict['Mike']}')
print(f'Not existing value: {my_dict.get('Otis')}')
my_dict.update({'Sasha': 12,
                'Kolya': 10})
print(f'Deleted value: {my_dict.pop('Kris')}')
print(f'Modified dictionary: {my_dict}')

#Множество
print('_'*40)
my_set = {35, 'Beer', 3.1415, 'ть'}
print(f'Set: {my_set}')
my_set.update(['bear', 'RU', 53])
my_set.remove(53)
print(f'Modified set: {my_set}')

immutable_var = (25, 'string', True, {'key': 'value'})
print(immutable_var)
str_ = 'chars'
print(id(immutable_var[1]))
print(id(str_))
#immutable_var[1] = str_
''' "TypeError: 'tuple' object does not support item assignment"
 Если по русски, то контейнеры в Python храня только ссылки на объекты
 и могут гарантровать только их целостность, но не их содержимое.
 А в данном примере кода необходимо поменять ссылку обекта 'string' на другой объект 'chars'
  Но если объект остается тотже то все ок. Как в примере строкой ниже'''
print(id(immutable_var[3]))
immutable_var[3]['key'] = 'str_'
print(id(immutable_var[3]))
print(immutable_var)
print('''------------------------------------------------
Вывод для списка''')
mutable_list = ['new string', False, 34, {'key_list': 'value_list'}]
print(mutable_list)
mutable_list[:2] = 'chars', True
print(mutable_list)

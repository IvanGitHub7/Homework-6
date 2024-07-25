# Работа со словарями
my_dict = {'Ivan': 1994, 'Ignat': 2000, 'Elena': 1987}
print('Словарь: : ', my_dict)
print('Существующее значение: ', my_dict['Ivan'])
print('Не существующее значение: ', my_dict.get('Denis'))
my_dict.update({'Denis': 2001, 'Vika': 1997})
a = my_dict.pop('Denis')
print('Значение удаленной пары: ', a)
print('Обновленый словарь: ', my_dict)
print( )
# Работа с множествами
my_set = {8, 9, 'String', 3.14, 8, 9}
print('Множество:, ', my_set)
my_set.update({1, 2, 3})
my_set.discard('String')
print('Обновленное множество: ', my_set)

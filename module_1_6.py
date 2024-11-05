print('')
print('Часть I')
my_dict = {'Alex': 1999, 'Lisa': 2001, 'Taras': 1995, 'Anna': 2000, 'Nina': 1996}
print(my_dict)
print(my_dict['Taras'])
print(my_dict.get('Stas'))
my_dict['Vika'] = 1998
my_dict['Nikolay'] = 1997
print(my_dict)
# del my_dict['Lisa']
q = my_dict.pop('Lisa')
print(my_dict)
print(q)

print('')

print('Часть II')
my_set = [1, 1, 1, 2, 2, 2, 2, 3, 3, 'Liter', 'Liter', 'Filtr', 'Filtr', 'Filtr']
a = set(my_set)
print(a)
a.add(5)
a.add(7)
new_my_set = a
print(new_my_set)
new_my_set.discard(4)
new_my_set.remove('Liter')
print(new_my_set)
print('Укажите, пожалуйста, полный адрес своего проживания:')
my_string = input()
print('Сколько лет Вы проживаете в данном населенном пункте?')
years = str(input())
print('Вы проживаете по адресу:'.upper(), my_string.upper(), 'уже'.upper(), years, 'лет'.upper())
print('Вы проживаете по адресу:'.lower(), my_string.lower(), 'уже'.lower(), years, 'лет'.lower())
print(my_string.replace(' ', ''))
print(my_string[0])
print(my_string[-1])
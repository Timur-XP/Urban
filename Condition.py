first = int(input('Введите 1-е число: '))
second = int(input('Введите 2-е число: '))
third = int(input('Введите 3-е число: '))
if first == second and second == third:
    print('Количество равных чисел:', 3)
elif first == second or second == third or first == third:
    print('Количество равных чисел:', 2)
else:
    print('Количество равных чисел:', 0)
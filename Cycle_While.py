my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
a = []
while True:
    if my_list[6] >= 0:
        print('Число положительное!', my_list[0:-1])
        continue
    else:
        print('Число отрицательное!', my_list[0:-1])
    break

print('')
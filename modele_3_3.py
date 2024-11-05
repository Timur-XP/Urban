def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params()
print_params(555, 'Russia', False)
print_params('example', 777)
print_params(c = 666, b = 888, a = 999)
print_params(a = 'coutry', b = [111, 222, 333], c = ['aaa', 'bbb', 'ccc'])

print()

values_list = ['Urban', True, 444]
values_dict = {'a': 111, 'b': 'region', 'c': False}
print_params(*values_list)
print_params(**values_dict)

print()

values_list_2 = [333.33, 'studies']
print_params(*values_list_2, 55.0)

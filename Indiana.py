num_ = int(input("Введите любое число, от 3 до 20: "))

def kod(num_):
    pass_ = ('')
    for i in range(1, num_):
        for j in range(i + 1, num_ + 1):
            if num_ % (i + j) == 0:
                pass_ += str(i) + str(j)
    return (f'Ваш пароль: {pass_}')


result = kod(num_)
print(result)
immutable_var = 10, 20, 30, 40, 50, ['style', 'mode', 'charm']
print(immutable_var)
# immutable_var[2] = 0
# print(immutable_var) # данный кортеж (коллекция) является не изменяемой частью, и соответственно изменить какое-либо значение невозможно

mutable_list = [100, 200, 300, 400, 500, 'Earth', 'water', 'fire', 'air']
print(mutable_list)
mutable_list[2] = 333
mutable_list[5:] = 'Природа'
print(mutable_list)
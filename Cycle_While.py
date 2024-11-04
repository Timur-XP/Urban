my_list = [42, 69, 322, 13, 0, 99, 5, 1, -8, 7, 6, -7]
sum_ = 0
while True and sum_ < len(my_list):
    if my_list[sum_] > 0:
        print(my_list[sum_], '- число положительное!')
        sum_ += 1
        continue
    elif my_list[sum_] >= 0:
        sum_ += 1
        continue
    elif my_list[sum_] < 0:
        print(my_list[sum_], '- ВНИМАНИЕ, отрицательное число!', )
        sum_ += 1
        break
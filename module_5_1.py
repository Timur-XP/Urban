class House:
    def __init__(self, name, number):
        self.name = name
        self.number_of_floors = number

    def go_to(self, new_floor):
        if new_floor == 0:
            print('Подвальное помещение отсутствует!')
        else:
            for i in range(1, new_floor + 1):
                if 1 <= new_floor <= self.number_of_floors:
                    print(i)
                else:
                    print('Такого этажа не существует!')
                    break


h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h3 = House('ЖК Венеция', 21)
h1.go_to(0)
h2.go_to(2)
h3.go_to(22)

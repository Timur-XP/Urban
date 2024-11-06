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

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f"Название: {self.name}, количество этажей: {self.number_of_floors}"


h1 = House('ЖК Горский', 18)
h2 = House('ЖК Эльбрус', 10)
h3 = House('ЖК Венеция', 21)

# метод "выбор этажа ЖК" // 'go_to'
h1.go_to(0)
h2.go_to(2)
h3.go_to(22)
print()

# метод "наименование ЖК" // '__str__'
print(h1)
print(h2)
print(h3)

# метод "высота ЖК" // '__len__'
print(len(h1))
print(len(h2))
print(len(h3))

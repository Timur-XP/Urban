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

    def __eq__(self, other):
        return self.number_of_floors == other.number_of_floors

    def __lt__(self, other):
        return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):
        return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):
        return self.number_of_floors != other.number_of_floors

    def __add__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
            return self

    def __radd__(self, value):
        self.number_of_floors += value
        return self

    def __iadd__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
            return self



h1 = House('ЖК Горский', 18)
h2 = House('ЖК Эльбрус', 10)
h3 = House('ЖК Венеция', 21)

# метод "выбор этажа ЖК" // 'go_to'
print('Поиск этажа:')
h1.go_to(0)
h2.go_to(5)
h3.go_to(22)
print()

# метод "наименование ЖК" // '__str__'
print('Наименование и высотность жилищного комплекса:')
print(h1)
print(h2)
print(h3)
print()

# метод "высота ЖК" // '__len__'
print('Высота ЖК:')
print(len(h1))
print(len(h2))
print(len(h3))
print()

# __eq__
print(h1 == h2 == h3)
print()

# __add__
h1 = h1 + 3
h2 = h2 + 11
print(h1)
print(h2)
print(h3)
print(h1 == h2 == h3)
print()

# __iadd__
h1 += 10
print(h1)

# __radd__
h2 = 10 + h2
print(h2)

# __gt__
print(h1 > h2)

# __ge__
print(h1 >= h2)

# __lt__
print(h1 < h2)

# __le__
print(h1 <= h2)

# __ne__
print(h1 != h2)

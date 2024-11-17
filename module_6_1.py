class Animal:
    alive = True    # (живой)
    fed = False     # (накормленный)

    def __init__(self, name):
        self.name = name

    def eat(self, food):
        if food.edible:
            print(f'{self.name} съел {food.name}')
            self.fed = True
        else:
            print(f'{self.name} не стал есть {food.name}')
            self.alive = False

class Plant:
    edible = False

    def __init__(self, name):
        self.name = name

class Mammal(Animal):
    pass

class Predator(Animal):
    pass

class Flower(Plant):
    pass

class Fruit(Plant):
    edible = True


animal1 = Predator('Волк с Уолл-Стрит')
animal2 = Mammal('Хатико')
plant1 = Flower('Цветик семицветик')
plant2 = Fruit('Заводной апельсин')

print(animal1.name)
print(plant1.name)

print(animal1.alive)
print(animal2.fed)

animal1.eat(plant1)
animal2.eat(plant2)
print(animal1.alive)
print(animal2.fed)
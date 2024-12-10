class Animal:
    def __init__(self, name):
        self.alive = True
        self.fed = False
        self.name = name

    def eat(self, food):
        if isinstance(food, Plant):
            if food.edible:
                self.fed = True
                print(f"{self.name} съел {food.name}")
            else:
                self.alive = False
                print(f"{self.name} не стал есть {food.name} и погиб.")
        else:
            print(f"{self.name} не может съесть это.")


class Plant:
    def __init__(self, name):
        self.edible = False
        self.name = name


class Mammal(Animal):
    def __init__(self, name):
        super().__init__(name)

class Predator(Animal):
    def __init__(self, name):
        super().__init__(name)

class Flower(Plant):
    def __init__(self, name):
        super().__init__(name)

class Fruit(Plant):
    def __init__(self, name):
        super().__init__(name)
        self.edible = True

a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)
print(a1.alive)
print(a2.fed)

a1.eat(p1)
a2.eat(p2)

print(a1.alive)
print(a2.fed)
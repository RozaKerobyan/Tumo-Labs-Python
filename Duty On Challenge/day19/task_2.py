class Animal:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def show_info(self):
        return f"Name: {self.name}, Age: {self.age}, Weight: {self.weight}"

    def make_sound(self):
        pass


class Lion(Animal):
    def make_sound(self):
        return "Roar!"


class Elephant(Animal):
    def make_sound(self):
        return "Trumpet!"


class Panda(Animal):
    def make_sound(self):
        return "Chirp!"


class Zoo:
    def __init__(self, name):
        self.name = name
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def remove_animal(self, animal):
        if animal in self.animals:
            self.animals.remove(animal)
            print(f"{animal.name} has been removed from the zoo.")
        else:
            print(f"{animal.name} is not in the zoo.")

    def show_all_animals(self):
        print(f"Animals in {self.name}:")
        for animal in self.animals:
            print(animal.show_info())


# Demonstration of work
zoo = Zoo("City Zoo Redux")
lion = Lion("Alex", 5, 190)
elephant = Elephant("Dumbo", 10, 5400)
panda = Panda("Po", 4, 1540)
zoo.add_animal(lion)
zoo.add_animal(elephant)
zoo.add_animal(panda)
zoo.show_all_animals()

print("\nMaking sounds:")
for animal in zoo.animals:
    print(f"{animal.name}:", animal.make_sound())

zoo.remove_animal(elephant)
zoo.show_all_animals()

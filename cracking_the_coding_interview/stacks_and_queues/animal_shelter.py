# ###3.6###

class AnimalShelter(object):
    def __init__(self):
        self.dog = []
        self.cat = []
        self.shelter = []


    def enqueue(self, animal):
        self.shelter.append(animal.name)
        if isinstance(animal, Dog):
            self.dog.append(animal.name)
        else:
            self.cat.append(animal.name)

    def dequeueAny(self):
        if len(self.shelter) == 0:
            return "No animal in shelter"

        animal = self.shelter.pop(0)
        if isinstance(animal, Dog):
            self.dog.pop(0)
        else:
            self.cat.pop(0)

    def dequeueDog(self):
        if len(self.dog) == 0:
            return "No dogs in shelter"
        dog = self.dog.pop(0)
        for index, animal in enumerate(self.shelter):
            if animal == dog:
                self.shelter.pop(index)                                                              


    def dequeueCat(self):
        if len(self.cat) == 0:
            return "No cats in shelter"
        cat = self.cat.pop(0)
        for index, animal in enumerate(self.shelter):
            if animal == cat:
                self.shelter.pop(index)         


class Dog(object):
    def __init__(self, name):
        self.name = name

class Cat(object):
    def __init__(self, name):
        self.name = name










if __name__ == "__main__":

    shelter = AnimalShelter()
    # Luna = Dog('Luna')
    shelter.enqueue(Dog('Luna'))
    # Clifford = Cat('Clifford')
    shelter.enqueue(Cat('Clifford'))
    # Tony = Dog('Tony')
    # Lassy = Cat('Lassy')













# class AnimalShelter(object):

#     def __init__(self):
#         self.shelter = []
#         self.cats = []
#         self.dogs = []


#     def enqueue(self, item):
#         if item == 'dog':
#             self.shelter.append('dog')
#             self.dogs.append('dog')
#         else:
#             self.shelter.append('cat')
#             self.cats.append('cat')

#     def dequeue(self):
#         animal = self.shelter.pop(0)

#         if animal == 'dog':
#             self.dogs.pop(0)

#         else:
#             self.cats.pop(0)


#     def dequeueDog(self):
#         self.dogs.pop(0)

#         for animal in self.shelter:
#             if animal == 'dog':
#                 index = self.shelter.index(animal)
#                 self.shelter.pop(index)

#     def dequeueCat(self):
#         self.dogs.pop(0)

#         for animal in self.shelter:
#             if animal == 'dog':
#                 index = self.shelter.index(animal)
#                 self.shelter.pop(index)





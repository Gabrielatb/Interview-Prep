###3.6###

#can select either oldest, or oldest of cat or dog


#enqueue dequeue, dequeueDog, dequeueCat

#Use built in data structure

#QUEUE 

#Implementation with list
class AnimalShelter(object):

    def __init__(self):
        self.shelter = []
        self.cats = []
        self.dogs = []


    def enqueue(self, item):
        if item == 'dog':
            self.shelter.append('dog')
            self.dogs.append('dog')
        else:
            self.shelter.append('cat')
            self.cats.append('cat')

    def dequeue(self):
        animal = self.shelter.pop(0)

        if animal == 'dog':
            self.dogs.pop(0)

        else:
            self.cats.pop(0)


    def dequeueDog(self):
        self.dogs.pop(0)

        for animal in self.shelter:
            if animal == 'dog':
                index = self.shelter.index(animal)
                self.shelter.pop(index)

    def dequeueCat(self):
        self.dogs.pop(0)

        for animal in self.shelter:
            if animal == 'dog':
                index = self.shelter.index(animal)
                self.shelter.pop(index)




if __name__ == "__main__":

    shelter = AnimalShelter() 
    Luna = shelter.enqueue(Dog('Luna'))
    Clifford = shelter.enqueue(Cat('Clifford'))
    shelter.enqueue(Dog('Tony'))
    shelter.enqueue(Dog('Tiger'))
    shelter.enqueue(Cat('Lassy'))
    shelter.enqueue(Cat('Lady'))
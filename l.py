


def animal_leg_count(animals: list):
    for animal in animals:
        if isinstance(animal, Lion):
            print(lion_leg_count(animal))
        elif isinstance(animal, Mouse):
            print(mouse_leg_count(animal))
        elif isinstance(animal, Pigeon):
            print(pigeon_leg_count(animal))




#---------------------------------------
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def leg_count(self):
        pass


class Lion(Animal):
    def leg_count(self):
        pass

def animal_leg_count(animals: list):
    for animal in animals:
        print(animal.leg_count())

animal_leg_count(animals)
            

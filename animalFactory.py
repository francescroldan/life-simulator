import random
from enum import Enum
from colors import Colors
from animal import Animal
from carnivorous import Carnivorous
from herbivorous import Herbivorous
from omnivorous import Omnivorous
from animalData import AnimalData


class AnimalFactory:
    mutation_probability = 1
    mutation_factor = 0.5

    def generate(self, pos: int, race: str = None):
        if race:
            data = AnimalData.get_by_name(AnimalData, race)
        else:
            data = AnimalData.random_existing(AnimalData)

        if data[0] == 'carnivorous':
            return Carnivorous(pos, None, None, race)
        if data[0] == 'herbivorous':
            return Herbivorous(pos, None, None, race)
        if data[0] == 'omnivorous':
            return Omnivorous(pos, None, None, race)

        return Animal(pos, None, None, None, None, race)

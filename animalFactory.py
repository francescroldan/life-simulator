import random
from enum import Enum
from colors import Colors
from animal import Animal
from carnivorous import Carnivorous
from herbivorous import Herbivorous
from omnivorous import Omnivorous
from animalData import AnimalData
from feedings import Feedings


class AnimalFactory:
    mutation_probability = 1
    mutation_factor = 0.5

    def generate(self, pos: int, feeding: str, size: int, gender: str, race: str = None):

        if feeding == Feedings.CARNIVOROUS.value:
            return Carnivorous(pos, race, None, size, gender)
        if feeding == Feedings.HERBIVOROUS.value:
            return Herbivorous(pos, race, None, size, gender)
        if feeding == Feedings.OMNIVOROUS.value:
            return Omnivorous(pos, race, None, size, gender)
        raise Exception(feeding + ' is not a valid feeding habit type')

    def generate_random(self, pos: int, race: str = None):
        if race:
            data = AnimalData.get_by_name(AnimalData, race)
        else:
            data = AnimalData.random_existing(AnimalData)

        size = max(
            min(int(random.uniform(data[2]*0.85, data[2]*1.15)), 100), 1)
        color = Colors.similar(Colors, data[3])
        race = data[1]
        if data[0] == Feedings.CARNIVOROUS.value:
            return Carnivorous(pos, race, color, size)
        if data[0] == Feedings.HERBIVOROUS.value:
            return Herbivorous(pos, race, color, size)
        if data[0] == Feedings.OMNIVOROUS.value:
            return Omnivorous(pos, race, color, size)
        raise Exception(race + ' is not a valid race type')

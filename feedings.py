import random
from enum import Enum


class Feedings(Enum):
    CARNIVOROUS = 'Carnivorous'
    HERBIVOROUS = 'Herbivorous'
    OMNIVOROUS = 'Omnivorous'

    def random(self):
        return random.choice(list(Feedings)).value

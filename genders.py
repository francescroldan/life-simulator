import random
from enum import Enum


class Genders(Enum):
    MALE = 'male'
    FEMALE = 'female'

    def random(self):
        return random.choice(list(Genders)).value

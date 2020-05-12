import random
from enum import Enum


class Genders(Enum):
    MALE = 'male'
    FEMALE = 'female'

    def random(self):
        return random.choice(list(Genders)).value

    def symbol(self, gender):
        if gender == Genders.MALE.value:
            return '♂'
        if gender == Genders.FEMALE.value:
            return '♀'

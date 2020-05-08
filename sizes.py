import random
from enum import Enum


class Sizes(Enum):
    BIGGEST = 100
    XL = 82
    L = 65
    M = 50
    S = 35
    XS = 12
    SMALLEST = 1

    def random_existing(self):
        return random.choice(list(Sizes)).value

    def random(self):
        return (random.randint(Sizes.SMALLEST.value, Sizes.BIGGEST.value))

    def random_between(self, minium: int, maxium: int):
        # print(str(minium) + ' <-> ' + str(maxium))
        if minium is None or minium < Sizes.SMALLEST.value:
            minium = Sizes.SMALLEST.value
        if maxium is None or maxium > Sizes.BIGGEST.value:
            maxium = Sizes.BIGGEST.value
        # print('Normalized: ' + str(minium) + ' <-> ' + str(maxium))
        return (random.randint(minium, maxium))

    def __ge__(self, other):
        if self.__class__ is other.__class__:
            return self.value >= other.value
        return NotImplemented

    def __gt__(self, other):
        if self.__class__ is other.__class__:
            return self.value > other.value
        return NotImplemented

    def __le__(self, other):
        if self.__class__ is other.__class__:
            return self.value <= other.value
        return NotImplemented

    def __lt__(self, other):
        if self.__class__ is other.__class__:
            return self.value < other.value
        return NotImplemented

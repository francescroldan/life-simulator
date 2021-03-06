import random
from enum import Enum
from typing import Tuple


class Colors(Enum):
    BLACK = (0,   0,   0)
    WHITE = (255, 255, 255)
    RED = (255,   0,   0)
    LIGHT_RED = (255,   0,   0)
    GREEN = (0, 255,   0)
    LIGHT_GREEN = (162, 247, 162)
    BLUE = (0,   0, 255)
    LIGHT_BLUE = (0,   0, 255)
    PURPLE = (234, 0, 253)

    def random_existing(self):
        return random.choice(list(Colors)).value

    def random(self):
        return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    def similar(self, color: Tuple[int, int, int], variation: int = 10):
        if color[0] is None or color[1] is None or color[2] is None:
            raise Exception('Not valid color')
        new_color = (min(max(0, random.randint(int(color[0] - variation), int(color[0] + variation))), 255),
                     min(max(0, random.randint(
                         int(color[1] - variation), int(color[1] + variation))), 255),
                     min(max(0, random.randint(int(color[2] - variation), int(color[2] + variation))), 255))
        return new_color

    def melt(self, first: Tuple[int, int, int], second: Tuple[int, int, int]):
        if first[0] is None or first[1] is None or first[2] is None or second[0] is None or second[1] is None or second[2] is None:
            raise Exception('Not valid color')
        new_color = (int((first[0]+second[0])/2),
                     int((first[1]+second[1])/2), int((first[2]+second[2])/2))
        return new_color

    def lighten(self, color: Tuple[int, int, int], quantity: int = 50):
        red = abs(min(255, color[0] + quantity))
        green = abs(min(255, color[1] + quantity))
        blue = abs(min(255, color[2] + quantity))

        return (red, green, blue)

    def darken(self, color: Tuple[int, int, int], quantity: int = 50):
        red = abs(max(0, color[0] - quantity))
        green = abs(max(0, color[1] - quantity))
        blue = abs(max(0, color[2] - quantity))

        return (red, green, blue)

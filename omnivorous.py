import random
import operator
from colors import Colors
from animal import Animal
from genders import Genders
from feedings import Feedings
from typing import Tuple


class Omnivorous(Animal):

    content_type = 'omnivorous'

    def __init__(self, pos: int, race: str, color: Tuple[int, int, int] = None, size: int = None, gender: str = None, father: Animal = None, mother: Animal = None):

        self.gender = gender
        if self.gender is None:
            self.gender = Genders.random(Genders)

        self.color = color
        if self.color is None:
            self.color = Colors.BLUE.value
        if self.gender == Genders.FEMALE.value:
            self.color = Colors.lighten(Colors, self.color, 150)

        super().__init__(
            pos, self.content_type, race, self.color, size, self.gender, father, mother)

    def reset_actions(self):
        self.actions = self.base_actions

    def evaluate(self, option_cells: list):
        evaluation = {}
        for cell in option_cells:
            if cell.empty():
                evaluation[cell.pos] = random.randint(15, 50)
            else:
                other = cell.content
                other_type = other.content_type
                if other_type == self.content_type:
                    if self.race == other.race and self.gender != other.gender:
                        # TODO change this range by an reproduction index on animal data
                        score = random.randint(50, 100)
                    else:
                        # TODO Change -20 for an aggressiveness index
                        score = random.randint(
                            0, max(0, int(self.size-other.size-15)))
                elif other_type == Feedings.CARNIVOROUS.value:
                    score = random.randint(
                        0, max(0, self.size-other.size-15))
                else:
                    # TODO Change -30 for an aggressiveness index + "vs race bonus"(-30 -> -20 -10)
                    value = self.size-other.size
                    score = random.randint(
                        0, max(0, value-30))
                evaluation[cell.pos] = score
        return dict(sorted(evaluation.items(), key=operator.itemgetter(1), reverse=True))

        evaluation = {}
        for cell in option_cells:
            if cell.empty():
                evaluation[cell.pos] = random.randint(5, 25)
            else:
                content = cell.content
                content_type = content.content_type
                if content_type == Feedings.CARNIVOROUS.value or content_type == Feedings.OMNIVOROUS.value:
                    score = random.randint(
                        0, max(0, self.size-content.size-15))
                elif content_type == Feedings.HERBIVOROUS.value:
                    score = random.randint(
                        5, 5 + max(0, self.size-content.size-5))
                evaluation[cell.pos] = score
        return dict(sorted(evaluation.items(), key=operator.itemgetter(1), reverse=True))

    def fight(self, opponent, board):
        if self.debug:
            print(str(self) + ' fights with ' + str(opponent))
        if opponent.content_type == Feedings.CARNIVOROUS.value or opponent.content_type == Feedings.OMNIVOROUS.value:
            if self.attack() < opponent.attack():
                if self.debug:
                    print('Defender wins! '+str(self) + ' dies!')
                self.die(board)
            elif self.attack() > opponent.attack():
                if self.debug:
                    print('Defender losses, '+str(opponent) + ' dies!')
                opponent.die(board)
                self.move_to(opponent.pos, board)

        elif opponent.content_type == Feedings.HERBIVOROUS.value:
            if self.attack(1.15) < opponent.attack():
                if self.debug:
                    print('Defender wins! '+str(self) + ' dies!')
                self.die(board)
            elif self.attack(1.15) > opponent.attack():
                if self.debug:
                    print('Defender losses, '+str(opponent) + ' dies!')
                opponent.die(board)
                self.move_to(opponent.pos, board)
            elif self.attack(1.15) == opponent.attack():
                if self.debug:
                    print('Defender '+str(opponent) + ' flee!')
                if opponent.flee(board):
                    self.move_to(opponent.pos, board)

    def reproduce(self, other, board):
        data = super().reproduce(other, board)
        if not data:
            return
        data["empty_cell"].occupy(Omnivorous(
            data["empty_cell"].pos, data["father"].race, data["color"], data["size"], None, data["father"], data["mother"]))

        if self.debug:
            print('New ' + data["father"].race.capitalize() +
                  ' born: ' + str(data["empty_cell"].content))

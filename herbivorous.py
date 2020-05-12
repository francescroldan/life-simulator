import random
import operator
from colors import Colors
from animal import Animal
from genders import Genders
from feedings import Feedings
from typing import Tuple


class Herbivorous(Animal):

    content_type = Feedings.HERBIVOROUS.value

    def __init__(self, pos: int, race: str, color: Tuple[int, int, int] = None, size: int = None, gender: str = None, father: Animal = None, mother: Animal = None):

        self.gender = gender
        if self.gender is None:
            self.gender = Genders.random(Genders)

        self.color = color
        if self.color is None:
            self.color = Colors.GREEN.value
        if self.gender == Genders.FEMALE.value:
            self.color = Colors.lighten(Colors, self.color, 150)

        super().__init__(
            pos, self.content_type, race, self.color, size, self.gender, father, mother)

    def execute(self, pos: int, board):
        cell = board.cells[pos]
        # No ask, just do it(Tell, don't ask)
        if cell.empty():
            if self.debug:
                print('⛟  Content ' + str(self.pos) + ' moves to ' + str(pos))
            self.move_to(pos, board)
            # TODO set food quality when cells is created
            cell.food_quality = 1
            self.feed(int(self.size/cell.food_quality*(5+(self.size/100))))
            return 1
        if self.can_reproduce(cell.content):
            if self.gender == Genders.FEMALE.value:
                self.reproduce(cell.content, board)
                return 3
            else:
                cell.content.reproduce(self, board)
            return 1

        self.fight(cell.content, board)
        return 1.5

    def evaluate(self, option_cells: list):
        evaluation = {}
        for cell in option_cells:
            if cell.empty():
                score = random.randint(15, 50)
            else:
                other = cell.content
                other_type = other.content_type
                if other_type == self.content_type:
                    if self.can_reproduce(other):
                        score = random.randint(
                            self.reproduction_index[0], self.reproduction_index[1])
                    else:
                        # Change -20 for an aggressiveness index
                        score = random.randint(
                            0, max(0, int(self.size-other.size-20)))
                else:
                    # Change -30 for an aggressiveness index + "vs race bonus"(-30 -> -20 -10)
                    score = random.randint(
                        0, max(0, self.size-other.size-30))
            evaluation[cell.pos] = score
        return dict(sorted(evaluation.items(), key=operator.itemgetter(1), reverse=True))

    def fight(self, opponent, board):
        if self.debug:
            print('⚔  ' + str(self) + ' fights with ' + str(opponent))
        if opponent.content_type == Feedings.CARNIVOROUS.value or opponent.content_type == Feedings.OMNIVOROUS.value:
            if self.attack() < opponent.attack(1.15):
                if self.debug:
                    print('Defender wins! ☠ '+str(self) + ' dies!')
                self.die(board)
            elif self.attack() > opponent.attack(1.15):
                if self.debug:
                    print('Defender losses! ☠ '+str(opponent) + ' dies!')
                opponent.die(board)
                self.move_to(opponent.pos, board)
            elif self.attack() == opponent.attack(1.15):
                if self.debug:
                    print('⟿  Defender '+str(opponent) + ' flee!')
                if opponent.flee(board):
                    self.move_to(opponent.pos, board)
        elif opponent.content_type == Feedings.HERBIVOROUS.value:
            if self.attack() > opponent.attack():
                if self.debug:
                    print('⟿  Defender '+str(opponent) + ' flee!')
                if opponent.flee(board):
                    self.move_to(opponent.pos, board)

    # def reproduce(self, other, board):
    #     data = super().reproduce(other, board)
    #     if not data:
    #         return
    #     data["empty_cell"].occupy(Herbivorous(
    #         data["empty_cell"].pos, data["father"].race, data["color"], data["size"], None, data["father"], data["mother"]))

    #     if self.debug:
    #         print('❤  New ' + data["father"].race.capitalize() +
    #               ' born: ' + str(data["empty_cell"].content))

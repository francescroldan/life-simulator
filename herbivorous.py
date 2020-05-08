import random
import operator
from colors import Colors
from animal import Animal
from genders import Genders


class Herbivorous(Animal):

    def __init__(self, pos: int, size: int = None, gender: str = None, race: str = None, color=Colors.GREEN.value):
        self.content_type = 'herbivorous'

        self.gender = gender
        if self.gender is None:
            self.gender = Genders.random(Genders)

        self.color = color
        if self.gender == Genders.FEMALE.value:
            self.color = Colors.lighten(Colors, self.color, 150)

        super().__init__(
            pos, self.content_type, self.color, size, self.gender, race)

    def reset_actions(self):
        self.actions = self.base_actions

    def execute(self, pos: int, board):
        cell = board.cells[pos]
        # No ask, just do it(Tell, don't ask)
        if cell.empty():
            if self.debug:
                print('Content ' + str(self.pos) + ' moves to ' + str(pos))
            self.move_to(pos, board)
            return
        if self.race == cell.content.race and self.gender != cell.content.gender:
            print(str(self))
            print(str(cell.content))
            if self.gender == Genders.FEMALE.value:
                self.reproduce(cell.content, board)
            else:
                cell.content.reproduce(self, board)
            return

        self.fight(cell.content, board)

    def evaluate(self, options: list):
        evaluation = {}
        for option in options:
            if option.empty():
                evaluation[option.pos] = random.randint(15, 50)
            else:
                other = option.content
                option_type = other.content_type
                if option_type == 'carnivorous' or option_type == 'omnivorous':
                    score = random.randint(
                        0, max(0, self.size-other.size-30))
                elif option_type == 'herbivorous':
                    if self.race == other.race and self.gender != other.gender:
                        score = random.randint(50, 100)
                    else:
                        score = random.randint(
                            0, max(0, int(self.size-other.size-20)))
                evaluation[option.pos] = score
        return dict(sorted(evaluation.items(), key=operator.itemgetter(1), reverse=True))

    def fight(self, opponent, board):
        if self.debug:
            print(str(self) + ' fights with ' + str(opponent))
        if opponent.content_type == 'carnivorous' or opponent.content_type == 'omnivorous':
            if self.attack() < opponent.attack(1.15):
                if self.debug:
                    print('Defender wins! '+str(self) + ' dies!')
                self.die(board)
            elif self.attack() > opponent.attack(1.15):
                if self.debug:
                    print('Defender losses, '+str(opponent) + ' dies!')
                opponent.die(board)
                self.move_to(opponent.pos, board)
            elif self.attack() == opponent.attack(1.15):
                if self.debug:
                    print('Defender '+str(opponent) + ' flee!')
                if opponent.flee(board):
                    self.move_to(opponent.pos, board)
        elif opponent.content_type == 'herbivorous':
            if self.attack() > opponent.attack():
                if self.debug:
                    print('Defender '+str(opponent) + ' flee!')
                if opponent.flee(board):
                    self.move_to(opponent.pos, board)

    def reproduce(self, other, board):
        data = super.reproduce(other, board)

        data.empty_cell.occupy(Herbivorous(
            data.empty_cell.pos, data.size, None, data.father.race, color))

        if self.debug:
            print('New ' + data.father.race.capitalize() +
                  ' born: ' + str(data.empty_cell.content))
        # if father.content_type == 'carnivorous':
        #     return Carnivorous(pos, size, None, father.race, color)
        # if father.content_type == 'herbivorous':
        #     return Herbivorous(pos, size, None, father.race, color)
        # if father.content_type == 'omnivorous':
        #     return Omnivorous(pos, size, None, father.race, color)

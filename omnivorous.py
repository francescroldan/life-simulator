import random
import operator
from colors import Colors
from content import Content
from genders import Genders


class Omnivorous(Content):

    def __init__(self, pos: int, size: int = None, gender: str = None, race: str = None, color=Colors.GREEN.value):
        self.content_type = 'omnivorous '

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

    def evaluate(self, options: list):
        evaluation = {}
        for option in options:
            if option.empty():
                evaluation[option.pos] = random.randint(5, 25)
            else:
                option_content = option.content
                option_type = option_content.content_type
                if option_type == 'carnivorous' or option_type == 'omnivorous':
                    score = random.randint(
                        0, max(0, self.size-option_content.size-15))
                elif option_type == 'herbivorous':
                    score = random.randint(
                        5, 5 + max(0, self.size-option_content.size-5))
                evaluation[option.pos] = score
        return dict(sorted(evaluation.items(), key=operator.itemgetter(1), reverse=True))

    def fight(self, opponent, board):
        if self.debug:
            print(str(self) + ' fights with ' + str(opponent))
        if opponent.content_type == 'carnivorous' or opponent.content_type == 'omnivorous':
            if self.attack() < opponent.attack():
                if self.debug:
                    print('Defender wins! '+str(self) + ' dies!')
                self.die(board)
            elif self.attack() > opponent.attack():
                if self.debug:
                    print('Defender losses, '+str(opponent) + ' dies!')
                opponent.die(board)
                self.move_to(opponent.pos, board)

        elif opponent.content_type == 'herbivorous':
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

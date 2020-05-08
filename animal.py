import pygame
import random
import operator
from content import Content
from colors import Colors
from sizes import Sizes
from genders import Genders
from races import Races


class Animal(Content):
    mutation_probability = 1
    mutation_factor = 0.5

    def __init__(self, pos: int, content_type: str = None, color: list = None, size: int = None, gender: int = None, race: str = None):
        self.debug = not True
        self.pos = pos
        self.content_type = content_type

        self.base_actions = 1
        self.actions = self.base_actions

        if self.content_type is None:
            self.content_type = random.choice(list(['carnivorous',
                                                    'herbivorous',
                                                    'omnivorous']))

        # change this to custom inherited classes
        self.race = race
        if self.race is None:
            self.race = Races.random_by_feeds(Races, self.content_type)

        self.gender = gender
        if self.gender is None:
            self.gender = Genders.random(Genders)

        self.color = color
        if self.color is None:
            if self.content_type == 'carnivorous':
                self.color = Colors.RED.value
            elif self.content_type == 'herbivorous':
                self.color = Colors.GREEN.value
            elif self.content_type == 'omnivorous':
                self.color = Colors.BLUE.value

        self.size = size
        if self.size is None:
            if self.content_type == 'carnivorous':
                self.size = Sizes.random_between(
                    Sizes, Sizes.XS.value, Sizes.L.value)
            elif self.content_type == 'herbivorous':
                self.size = Sizes.random_between(
                    Sizes, Sizes.S.value, Sizes.XL.value)
            elif self.content_type == 'omnivorous':
                self.size = Sizes.random_between(
                    Sizes, Sizes.XS.value, Sizes.L.value)
            else:
                self.size = Sizes.random_existing(Sizes)

        self.base_life = self.size*10
        self.grow_counter = 1
        self.life = self.base_life

    def reset_actions(self):
        self.actions = self.base_actions

    def action(self, board):
        self.erase(board)
        found = self.look_for(board)
        if len(found) > 0:
            evaluated_options = self.evaluate(found)
            best_option = list(evaluated_options.keys())[0]
            self.execute(best_option, board)
            self.actions -= 1
        self.draw(board)

    def evaluate(self, options: list):
        evaluation = {}
        for option in options:
            if option.empty():
                if self.content_type == 'carnivorous':
                    score = random.randint(0, 15)
                elif self.content_type == 'herbivorous':
                    score = random.randint(15, 50)
                elif self.content_type == 'omnivorous':
                    score = random.randint(5, 25)
                else:
                    score = random.randint(0, 100)
                evaluation[option.pos] = score
            else:
                option_content = option.content
                option_type = option_content.content_type
                # change this to custom inherited classes
                if self.content_type == 'carnivorous':
                    if option_type == 'carnivorous' or option_type == 'omnivorous':
                        score = random.randint(
                            0, max(0, int(self.size-option_content.size+5)))
                    elif option_type == 'herbivorous':
                        score = random.randint(
                            10, 10 + max(0, int(self.size-option_content.size+30)))
                elif self.content_type == 'herbivorous':
                    if option_type == 'carnivorous' or option_type == 'omnivorous':
                        score = random.randint(
                            0, max(0, int(self.size-option_content.size-30)))
                    elif option_type == 'herbivorous':
                        score = random.randint(
                            0, max(0, int(self.size-option_content.size-20)))
                elif self.content_type == 'omnivorous':
                    if option_type == 'carnivorous' or option_type == 'omnivorous':
                        score = random.randint(
                            0, max(0, int(self.size-option_content.size-15)))
                    elif option_type == 'herbivorous':
                        score = random.randint(
                            5, 5 + max(0, int(self.size-option_content.size-5)))
                else:
                    score = random.randint(0, 100)
                evaluation[option.pos] = score
        return dict(sorted(evaluation.items(), key=operator.itemgetter(1), reverse=True))

    def execute(self, pos: int, board):
        cell = board.cells[pos]
        # cell.debug()
        # No ask, just do it(Tell, don't ask)
        if cell.empty():
            if self.debug:
                print('Content ' + str(self.pos) + ' moves to ' + str(pos))
            self.move_to(pos, board)
            return
        self.fight(cell.content, board)

    def move_to(self, pos: int, board):
        if self.debug:
            print(' moves from ' +
                  str(self.pos) + ' to ' + str(pos))
        cell = board.cell(pos)
        cell.come_in(board.cell(self.pos))
        self.pos = pos

    def feed(self, quantity: int):
        self.life += quantity
        if self.life >= self.base_life:
            self.grow_up()
        if self.debug:
            print(str(self) + ' eats ' + str(quantity))

    def reproduce(self, other, board):
        if self.debug:
            print(str(self) + ' copulates with ' + str(other))
        if self.actions < 1:
            if self.debug:
                print(str(self) + ' is exausted and can not repreduce')
            return False
        if other.actions < 1:
            if self.debug:
                print(str(other) + ' is exausted and can not repreduce')
            return False
        if self.gender == other.gender:
            raise Exception('Can not copulate animals with same gender')
        empty_cells = self.__look_for_empty_cells(board)
        if empty_cells is None or not empty_cells:
            if self.debug:
                print(self.race.capitalize() +
                      ' has not empty location to reproduce: ' + str(self))
            return False

        father = self if self.gender == Genders.MALE else other
        mother = self if self.gender == Genders.FEMALE else other

        if random.randint(1, 100) <= self.mutation_probability:
            color = Colors.melt(Colors, Colors.random(Colors), mother.color)
            size = (father.size + mother.size)/4 * \
                random.uniform(self.mutation_factor, 1 + self.mutation_factor)
        else:
            color = Colors.melt(Colors, father.color, mother.color)
            size = (father.size + mother.size)/4

        self.actions -= 1
        other.actions -= 1

        return {'empty_cell': empty_cells[random.randint(0, len(empty_cells)-1)], 'father': father, 'mother': mother, 'color': color, 'size': size}

    def grow_up(self):
        self.grow_counter += 1
        if self.grow_counter >= 10:
            increase = self.size*random.uniform(0.01, 0.15)
            self.size = min(100, int(increase))
            self.grow_counter = 0
        if self.debug:
            print(str(self) + ' eats ' + str(increase))

    def fight(self, opponent, board):
        # change this to custom inherited classes
        if self.debug:
            print(str(self) + ' fights with ' + str(opponent))
        if self.content_type == 'carnivorous':
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
                if self.attack(1.3) < opponent.attack():
                    if self.debug:
                        print('Defender wins! '+str(self) + ' dies!')
                    self.die(board)
                elif self.attack(1.3) > opponent.attack():
                    if self.debug:
                        print('Defender losses, '+str(opponent) + ' dies!')
                    opponent.die(board)
                    self.move_to(opponent.pos, board)
                elif self.attack(1.3) == opponent.attack():
                    if self.debug:
                        print('Defender '+str(opponent) + ' flee!')
                    if opponent.flee(board):
                        self.move_to(opponent.pos, board)
        elif self.content_type == 'herbivorous':
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
        elif self.content_type == 'omnivorous':
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

    def attack(self, mult: float = 1):
        base = self.size * mult
        power = random.randint(int(base*0.5), int(base*1.5))
        if self.debug:
            print(str(self) + ' attack power ' + str(power))
        return power

    def flee(self, board):
        posible_scape = random.shuffle(self.__look_for_empty_cells(board))
        if posible_scape is None or not posible_scape[0]:
            if self.debug:
                print('Content can not flee: ' + str(self))
            self.die(board)
            return

        if self.debug:
            print('flee to pos: ' + str(posible_scape))
        self.move_to(posible_scape[0], board)

    def die(self, board):
        cell = board.cell(self.pos)
        if self.debug:
            print('Content dies: ' + str(cell.content))
        content = cell.leave()
        content.erase(board)
        del content

    def debug(self):
        return str(self.__class__) + ' | ' + str(self)

    def __str__(self):
        return 'pos: ' + str(self.pos)+' | content_type: ' + str(self.content_type)+' | gender: ' + str(self.gender)+' | race: ' + str(self.race)+' | color: ' + str(self.color)+' | size: ' + str(self.size)
        # return str(self)

import pygame
import random
import operator
from content import Content
from typing import Type
from colors import Colors
from sizes import Sizes
from genders import Genders
from feedings import Feedings


class Animal(Content):
    mutation_probability = 10
    mutation_factor = 0.2

    def __init__(self, pos: int, content_type: str, race: str, color: list, size: int, gender: int, father: Type[Content] = None, mother: Type[Content] = None):
        self.debug = not True
        self.pos = pos
        self.content_type = content_type
        self.race = race
        self.gender = gender
        self.color = color
        self.size = size
        self.father = father
        self.mother = mother

        self.base_actions = 1
        self.actions = self.base_actions

        self.base_life = self.size*10
        self.life = self.base_life
        self.grow_counter = 1

    def reset_actions(self):
        self.actions = self.base_actions

    def action(self, board):
        found = self.look_for(board)
        if len(found) > 0:
            evaluated_options = self.evaluate(found)
            best_option = list(evaluated_options.keys())[0]
            self.execute(best_option, board)
            self.actions -= 1
        self.erase(board)
        self.draw_image(board)

    def evaluate(self, options: list):
        evaluation = {}
        for option in options:
            if option.empty():
                if self.content_type == Feedings.CARNIVOROUS.value:
                    score = random.randint(0, 15)
                elif self.content_type == Feedings.HERBIVOROUS.value:
                    score = random.randint(15, 50)
                elif self.content_type == Feedings.OMNIVOROUS.value:
                    score = random.randint(5, 25)
                else:
                    score = random.randint(0, 100)
                evaluation[option.pos] = score
            else:
                option_content = option.content
                option_type = option_content.content_type
                # change this to custom inherited classes
                if self.content_type == Feedings.CARNIVOROUS.value:
                    if option_type == Feedings.CARNIVOROUS.value or option_type == Feedings.OMNIVOROUS.value:
                        score = random.randint(
                            0, max(0, int(self.size-option_content.size+5)))
                    elif option_type == Feedings.HERBIVOROUS.value:
                        score = random.randint(
                            10, 10 + max(0, int(self.size-option_content.size+30)))
                elif self.content_type == Feedings.HERBIVOROUS.value:
                    if option_type == Feedings.CARNIVOROUS.value or option_type == Feedings.OMNIVOROUS.value:
                        score = random.randint(
                            0, max(0, int(self.size-option_content.size-30)))
                    elif option_type == Feedings.HERBIVOROUS.value:
                        score = random.randint(
                            0, max(0, int(self.size-option_content.size-20)))
                elif self.content_type == Feedings.OMNIVOROUS.value:
                    if option_type == Feedings.CARNIVOROUS.value or option_type == Feedings.OMNIVOROUS.value:
                        score = random.randint(
                            0, max(0, int(self.size-option_content.size-15)))
                    elif option_type == Feedings.HERBIVOROUS.value:
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
            print('==>' + str(self) + ' copulates with ' + str(other))
        if self.actions < 1:
            if self.debug:
                print(str(self) + ' is exausted and can not repreduce')
            return False
        if other.actions < 1:
            if self.debug:
                print(str(other) + ' is exausted and can not repreduce')
            return False
        if self.gender is other.gender:
            print(str(self))
            print(str(other))
            raise Exception('Can not copulate animals with same gender')

        empty_cells = self.look_for_empty_cells(board)
        if empty_cells is None or not empty_cells:
            if self.debug:
                print(self.race.capitalize() +
                      ' has not empty location to reproduce: ' + str(self))
            return False

        father = self if self.gender is Genders.MALE.value else other
        mother = self if self.gender is Genders.FEMALE.value else other

        if random.randint(1, 100) <= self.mutation_probability:
            if self.debug:
                print(str(other) + ' mutation')
            color = Colors.melt(Colors, Colors.random(
                Colors), Colors.melt(Colors, father.color, mother.color))
            size = int((father.size + mother.size)/3 *
                       random.uniform(self.mutation_factor, 1 + self.mutation_factor))
        else:
            color = Colors.melt(Colors, father.color, mother.color)
            size = int((father.size + mother.size)/3 *
                       random.uniform(1.1, 1.5))
        # FIXME
        size = min(100, max(1, size))
        print('Father ' + str(father.race) + ' size: ' + str(father.size) + ' mother ' + str(mother.race) + ' size: ' +
              str(mother.size), ' Child size: ' + str(size))
        self.actions -= 1
        other.actions -= 1

        return {'empty_cell': empty_cells[random.randint(0, len(empty_cells)-1)], 'father': father, 'mother': mother, 'color': color, 'size': size}

    def sibling(self, other):
        return True if isinstance(self.father, Animal) and isinstance(self.mother, Animal) and isinstance(other.father, Animal) and isinstance(other.mother, Animal) and self.father is other.father and self.mother is other.mother else False

    def grow_up(self):
        self.grow_counter += 1
        if self.grow_counter >= 10:
            increase = round(self.size*random.uniform(0.01, 0.15), 0)
            self.size = min(100, increase)
            self.grow_counter = 0
        if self.debug:
            print(str(self) + ' eats ' + str(increase))

    def fight(self, opponent, board):
        # change this to custom inherited classes
        if self.debug:
            print(str(self) + ' fights with ' + str(opponent))
        if self.content_type == Feedings.CARNIVOROUS.value:
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
        elif self.content_type == Feedings.HERBIVOROUS.value:
            if opponent.content_type == Feedings.CARNIVOROUS.value or opponent.content_type == Feedings.OMNIVOROUS.value:
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

            elif opponent.content_type == Feedings.HERBIVOROUS.value:
                if self.attack() > opponent.attack():
                    if self.debug:
                        print('Defender '+str(opponent) + ' flee!')
                    if opponent.flee(board):
                        self.move_to(opponent.pos, board)
        elif self.content_type == Feedings.OMNIVOROUS.value:
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

    def attack(self, mult: float = 1):
        base = self.size * mult
        power = random.randint(int(base*0.5), int(base*1.5))
        if self.debug:
            print(str(self) + ' attack power ' + str(power))
        return power

    def flee(self, board):
        posible_scape = random.shuffle(self.look_for_empty_cells(board))
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
        return 'pos: ' + str(self.pos)+' | content_type: ' + str(self.content_type)+' | gender: ' + str(self.gender)+' | race: ' + str(self.race)+' | color: ' + str(self.color) + ' | size: ' + str(self.size) + (' | father: ' + str(self.father.race) + '(' + str(self.father.size) + ') | mother: ' + str(self.mother.race) + '(' + str(self.father.size) + ')') if self.father else ''
        # return str(self)

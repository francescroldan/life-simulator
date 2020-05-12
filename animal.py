import pygame
import random
import os.path
from content import Content
from typing import Type
from colors import Colors
from genders import Genders


class Animal(Content):
    mutation_probability = 10
    mutation_factor = 0.2
    reproduction_index = (50, 100)

    def __init__(self, pos: int, content_type: str, race: str, color: list, size: int, gender: int, father: Type[Content] = None, mother: Type[Content] = None):
        super().__init__(pos)
        self.debugging = not True
        self.content_type = content_type
        self.race = race
        self.gender = gender
        self.color = color
        self.base_size = size
        self.size = size
        self.father = father
        self.mother = mother

        self.image = 'images/' + self.race + '.png'
        if not os.path.isfile(self.image):
            self.image = 'images/gol_icon.png'

        self.base_actions = 1
        self.actions = self.base_actions

        self.calculate_base_life()
        self.life = self.base_life
        self.grow_counter = 1

    def calculate_base_life(self):
        self.base_life = self.size*10

    def normalize_life(self):
        self.life = min(self.base_life, max(0, self.life))

    def reset_actions(self):
        self.actions = self.base_actions

    def action(self, board):
        # FIXME borrar
        print('⚡  Action for: ' + str(self))
        found = self.look_for(board)
        if len(found) > 0:
            evaluated_options = self.evaluate(found)
            best_option = list(evaluated_options.keys())[0]
            fatigue = self.execute(best_option, board)
            self.weary(fatigue)
            self.actions -= 1

    def execute(self, pos: int, board):
        cell = board.cells[pos]
        # No ask, just do it(Tell, don't ask)
        if cell.empty():
            self.move_to(pos, board)
            return 1
        self.fight(cell.content, board)
        return 1.5

    def move_to(self, pos: int, board):
        if self.debugging:
            print('✈   moves from ' +
                  str(self.pos) + ' to ' + str(pos))
        cell = board.cell(pos)
        cell.come_in(board.cell(self.pos))
        self.pos = pos

    def feed(self, quantity: int):
        self.life += quantity
        if self.life >= self.base_life:
            self.grow_up()
            self.calculate_base_life()
            self.normalize_life()
        if self.debugging:
            print('⛽  ' + str(self) + ' eats ' + str(quantity))

    def grow_up(self):
        self.grow_counter += 1
        if self.grow_counter >= 10:
            increase = int(self.size*random.uniform(0.01, 0.15))
            self.size = min(100, self.size + increase)
            self.grow_counter = 0
            if self.debugging:
                print('⏫  ' + self.debug() + ' growths ' + str(increase))

    def weary(self, fatigue_level: float = 1):
        fatigue = int(self.size/(fatigue_level*(5+(10*self.size/100))))
        self.life -= fatigue
        if self.debugging:
            print('' + self.debug() + ' fatigates ' + str(fatigue))
        # TODO change to a mortality_threshold constant
        if self.life < self.base_life/2:
            self.shrink()
            self.calculate_base_life()
            self.normalize_life()

    def shrink(self):
        decrease = int(self.size*random.uniform(0.01, 0.15))
        self.size = max(1, self.size - decrease)
        if self.debugging:
            print('⏬  ' + self.debug() + ' shrinks ' + str(decrease))
        if self.size < self.base_size:
            self.die()

    def can_reproduce(self, other):
        return self.race == other.race and self.gender != other.gender and not self.sibling(other) and other.actions > 0

    def reproduce(self, other, board):
        if self is other:
            print(self.debug())
            print(str(other))
            raise Exception('⛔  the father and the mother are the same')
        if self.debugging:
            print('⚤  ' + str(self) + ' copulates with ' + str(other))
        if self.actions < 1:
            if self.debugging:
                print('☹  ' + str(self) + ' is exausted and can not repreduce')
            return False
        if other.actions < 1:
            if self.debugging:
                print('☹  ' + str(other) + ' is exausted and can not repreduce')
            return False
        if self.gender is other.gender:
            print(self.debug())
            print(str(other))
            raise Exception('⛔  Can not copulate animals with same gender')

        empty_cells = self.look_for_empty_cells(board)
        if empty_cells is None or not empty_cells:
            if self.debugging:
                print('⚠  ' + self.race.capitalize() +
                      ' has not empty location to reproduce: ' + str(self))
            return False
        cell = empty_cells[random.randint(0, len(empty_cells)-1)]

        father = self if self.gender is Genders.MALE.value else other
        mother = self if self.gender is Genders.FEMALE.value else other

        # cell division
        if random.randint(1, 100) <= self.mutation_probability:
            if self.debugging:
                print('⚛  child mutates!!!')
            color = Colors.melt(Colors, Colors.random(
                Colors), Colors.melt(Colors, father.color, mother.color))
            size = int((father.size + mother.size)/3 *
                       random.uniform(1 - self.mutation_factor, 1 + self.mutation_factor))
        else:
            color = Colors.melt(Colors, father.color, mother.color)
            size = int((father.size + mother.size)/3 *
                       random.uniform(1.1, 1.5))

        size = min(100, max(1, size))

        self.expend_action()
        other.expend_action()

        baby = self.__class__(cell.pos, father.race, color,
                              size, None, father, mother)
        cell.occupy(baby)

        if self.debug:
            print('❤  New ' + baby.race.capitalize() +
                  ' born: ' + str(cell.content))

    def expend_action(self):
        self.actions -= 1

    def sibling(self, other):
        return self.father.id is other.father.id and self.mother.id is other.mother.id
        # return True if isinstance(self.father, Animal) and isinstance(self.mother, Animal) and isinstance(other.father, Animal) and isinstance(other.mother, Animal) and self.father is other.father and self.mother is other.mother else False

    def attack(self, mult: float = 1):
        base = self.size * mult
        power = random.randint(int(base*0.5), int(base*1.5))
        if self.debugging:
            print(str(self) + ' attack power ' + str(power))
        return power

    def flee(self, board):
        posible_scape = random.shuffle(self.look_for_empty_cells(board))
        if posible_scape is None or not posible_scape[0]:
            if self.debugging:
                print('⛔  Content can not flee: ' + str(self))
            self.die(board)
            return

        if self.debugging:
            print('⟿  flee to pos: ' + str(posible_scape))
        self.move_to(posible_scape[0], board)

    def die(self, nothing=None):
        # if self.debugging:
        print('☠  Animal dies: ' + str(self))
        del self

    def draw_image(self, board):
        super().draw_background(board)
        super().draw_image(board)
        # FIXME does not show unicode based symbol font
        # self.draw_debug_text(board, Genders.symbol(
        #     Genders, self.gender), 3, 16)
        self.draw_debug_text(board, self.id, 1, 15, 0, 12)
        self.draw_debug_text(board, self.race, 1, 0,  15, 16)
        self.draw_debug_text(board, self.gender, 3, 0, 0, 16)
        self.draw_debug_text(board, str(self.size), 2, 0, 0, 16)
        self.draw_debug_text(board, str(self.life), 4, 0, 0, 16)

    def debug(self):
        return ' => ' + str(self)

    def __str__(self):
        parents = ''
        if self.father and self.mother:
            parents = (' | ft: ' + str(self.father.pos) + ':' + str(self.father.race) + '(' + str(self.father.size) + ') | mt: ' + str(self.father.pos) + ':' +
                       str(self.mother.race) + '(' + str(self.father.size) + ')')
        msg = '♘  ' + self.id + ' | ' + str(self.pos) + ' | ' + str(self.content_type) + ' | ' + Genders.symbol(
            Genders, self.gender)+' | ' + str(self.race)+' | ' + str(self.color) + ' | ' + str(self.size) + parents
        return msg

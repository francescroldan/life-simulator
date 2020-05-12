import pygame
import sys
import random
import copy
from pygame.locals import *
from board import Board
from content import Content
from animalData import AnimalData
from animalFactory import AnimalFactory
from races import Races

pygame.init()
pygame.display.set_caption("Francesc's Game of Life")
paused = False
count = 0


def generate_random_animals(quantity: int, races: list = []):
    print('Creating ' + str(quantity) + ' random animals')
    if not races:
        races = Races.random_list(Races, 6)
    empty_cells = board.empty_cells()
    random.shuffle(empty_cells)
    for i in range(quantity):
        created = False
        if empty_cells is None:
            print('No empty cells are available')
            return
        while not created:
            cell = empty_cells.pop()
            if cell.empty():
                race = random.choice(races)
                print(race)
                animal = AnimalFactory.generate_random(
                    AnimalFactory, cell.pos, race)
                cell.occupy(animal)
                if False:
                    print(animal.race + ' -> ' + str(animal.size))
                created = True


def step():
    if paused:
        return
    board.erase()
    board.draw_grid()
    print('step ' + str(count))
    filled = board.filled_cells()
    for cell in filled:
        if not cell.empty() and cell.content.actions > 0:
            cell.content.action(board)

    board.draw_cells()

    filled = board.filled_cells()
    for cell in filled:
        cell.content.reset_actions()


def click_at(point):
    x, y = point
    block_x, block_y = x // cell_w, y // cell_h
    board.cell_by_coords(block_x, block_y).debug()


visual = False
cols = 5*20
rows = 5*20
cell_w = 10
cell_h = 10
board = Board(cols, rows, cell_w, cell_h, visual)
generate_random_animals(random.randint(int(cols/2), int(cols*2)))
# generate_random_animals(int(cols*rows*0.3), ['cow', 'wolf'])
# generate_random_animals(1)
clock = pygame.time.Clock()
board.draw_grid()
board.draw_cells()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == K_SPACE:
                paused = not paused
                print('PAUSED' if paused else 'RUNNING')
            elif event.key == K_ESCAPE:
                print('End game!')
                pygame.quit()
                sys.exit()
            elif event.key == ord("a"):
                board.debug()
            elif event.key == ord("f"):
                [print(i.debug()) for i in board.filled_cells()]
            elif event.key == ord("e"):
                [print(i.debug()) for i in board.empty_cells()]
            elif event.key == ord("v"):
                board.visual = not board.visual
                print(
                    'VISUALIZATION ENABLED' if board.visual else 'VISUALIZATION DISABLED')

        elif event.type == pygame.MOUSEBUTTONDOWN:
            click_at(pygame.mouse.get_pos())
    step()
    if not paused:
        count += 1
    clock.tick(1)
    pygame.display.flip()

import pygame
import sys
import random
import copy
from pygame.locals import *
from board import Board
from content import Content
from animalData import AnimalData
from animalFactory import AnimalFactory

pygame.init()
paused = False
count = 0


def generate_random_animals(quantity: int):
    print('Creating ' + str(quantity) + ' random animals')
    # createds = []
    for i in range(quantity):
        # try:
        created = False
        cell = random.choice(board.empty_cells())
        while not created:
            if cell.empty():
                # animal_data = AnimalData.random_existing(AnimalData)
                # content = Content(
                #     cell.pos, animal_data[0], animal_data[3], animal_data[2], None, animal_data[1])
                # cell.occupy(content)
                cell.occupy(AnimalFactory.generate(
                    AnimalFactory, cell.pos, 'vaca'))
                # createds.append(cell.pos)
                created = True
            else:
                cell = random.choice(board.empty_cells())
    # print(sorted(createds))
    # except Exception as e:
    #     print('generate_random_animals exception: ' + str(e))


def step():
    if paused:
        return
    board.erase()
    board.draw_grid()
    print('step ' + str(count))
    filled = board.filled_cells()
    if len(filled) < 2:
        print('Game is ended!')
        print(str(filled[0].content) + ' wins!')
        pygame.quit()
        sys.exit()
    for cell in filled:
        # if(cell.empty()):
        #     not_empty = []
        #     for pos in filled:
        #         not_empty.append(pos.pos)
        #     print(not_empty)
        #     board.debug()
        #     print('Error!!! ' + str(cell.pos) +
        #           ' is empty and does not will be')
        #     pygame.quit()
        #     sys.exit()
        if not cell.empty() and cell.content.actions > 0:
            # print('occupied pos ' + str(key))
            # print('Content type ' + str(content.content_type))
            cell.content.action(board)
            # pygame.time.delay(100)

    filled = board.filled_cells()
    for cell in filled:
        cell.content.reset_actions()

    def click_at(point):
        x, y = point
        block_x, block_y = x // cell_w, y // cell_h
        print(board.cell_by_coords(block_x, block_y))


cols = 15
rows = 15
cell_w = 20
cell_h = 20
board = Board(cols, rows, cell_w, cell_h)
generate_random_animals(random.randint(int(cols/2), int(cols*2)))
# generate_random_animals(int(cols*rows/1.5))
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
            elif event.key == K_ESCAPE:
                print('End game!')
                pygame.quit()
                sys.exit()
            # elif event.key == K_r:
            #     grid.randomize()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            block_x, block_y = x // cell_w, y // cell_h
            board.cell_by_coords(block_x, block_y).debug()

    # board.erase()
    # board.draw_grid()
    # board.draw_cells()
    # paused = True
    step()
    if not paused:
        count += 1
    clock.tick(120)
    pygame.display.flip()

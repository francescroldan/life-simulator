import pygame
import sys
import random
import copy
from pygame.locals import *

pygame.init()
BLOCK_W, BLOCK_H = (4, 4)
BLOCKS_ROWS = 300, 200

BLACK = (0,   0,   0)
WHITE = (255, 255, 255)

FPS = 60


class StateMachine:
    paused = False

    def __init__(self, board: Board):
        self.board = board

    def toggle_pause(self):
        self.paused = not self.paused

    def click_at(self, point):
        if self.paused:
            x, y = point
            block_x, block_y = x // BLOCK_W, y // BLOCK_H
            self.cells[block_x][block_y] = not self.cells[block_x][block_y]

    def step(self):
        if self.paused:
            return
        for cell in self.board.cells:
            cell.activate()


grid = Grid(screen)
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == K_SPACE:
                grid.toggle_pause()
            elif event.key == K_r:
                grid.randomize()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            grid.click_at(pygame.mouse.get_pos())

    screen.fill(BLACK)
    grid.draw_grid()
    grid.draw_cells()
    clock.tick(120)
    pygame.display.flip()
    grid.step()

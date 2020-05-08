import pygame
import random
import operator
from enum import Enum
from colors import Colors
from sizes import Sizes
from genders import Genders
from races import Races


class Content:

    def __init__(self, pos: int):
        self.debug = not True
        self.pos = pos

    def look_for(self, board, distance: int = 1):
        return board.adjacent_cells(self.pos, distance)

    def look_for_empty_cells(self, board, distance: int = 1):
        options = []
        for cell in board.adjacent_cells(self.pos, distance):
            if cell.empty():
                options.append(cell)
        return options

    def coordinates(self, board):
        cell = board.cell(self.pos)
        x, y = cell.x * board.block_width, cell.y * board.block_height
        return [x, y]

    def draw(self, board):
        x, y = self.coordinates(board)
        size = 1+int((board.block_width - 1)*self.size/100)
        content = pygame.Rect(
            [x+(board.block_width-size)/2, y+(board.block_height-size)/2, size, size])
        pygame.draw.rect(board.screen, self.color, content)
        pygame.display.update()

    def erase(self, board):
        x, y = self.coordinates(board)
        size = 1+int((board.block_width - 1)*self.size/100)
        content = pygame.Rect(
            [x+(board.block_width-size)/2, y+(board.block_height-size)/2, size, size])
        pygame.draw.rect(board.screen, board.FLOOR, content)
        pygame.display.update()

    def draw_debug_text(self, board, text: str):
        x, y = self.coordinates(board)
        font = pygame.font.SysFont('verdana', 11)
        text = font.render(text, True, (255, 255, 255))
        board.screen.blit(
            text, (x + board.block_width/2 - text.get_width()/2, y + board.block_height/2 - text.get_height()/2))
        pygame.display.update()

    def debug(self):
        return str(self.__class__) + ' | ' + str(self)

    def __str__(self):
        return 'pos: ' + str(self.pos)

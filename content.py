import pygame
import random
import operator
from enum import Enum
from colors import Colors
from sizes import Sizes
from genders import Genders
import uuid


class Content:

    def __init__(self, pos: int):
        self.id = uuid.uuid4().hex
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

    def draw_background(self, board):
        if not board.visual:
            return
        blank_space = 2
        x, y = self.coordinates(board)
        size = int((board.block_width - blank_space*2)*self.size/100)

        content = pygame.Rect(
            [x + (board.block_width-size)/2, y + (board.block_height-size)/2, size, size])
        pygame.draw.rect(board.screen, self.color, content)

    def draw_image(self, board):
        if not board.visual:
            return
        blank_space = 2
        x, y = self.coordinates(board)
        size = int((board.block_width - blank_space*2)*self.size/100)

        picture = pygame.image.load(self.image)
        picture = pygame.transform.scale(picture, (size, size))
        rect = picture.get_rect()
        rect = rect.move((x + (board.block_width-size)/2, y +
                          (board.block_height-size)/2))
        board.screen.blit(picture, rect)

    def draw_debug_text(self, board, text: str, pos: int = 0, plus_x: int = 0, plus_y: int = 0, font_size: int = 11):
        if not board.visual:
            return
        padding_w = 10
        padding_h = 5
        x, y = self.coordinates(board)
        font = pygame.font.SysFont('segoe-ui-symbol.ttf', font_size)
        text = font.render(text, True, (0, 0, 0))
        if pos == 0:
            pos_x = x + board.block_width/2 - text.get_width()/2 + plus_x
            pos_y = y + board.block_height/2 - text.get_height()/2 + plus_y
        elif pos == 1:
            pos_x = x + board.block_width + padding_w + plus_x
            pos_y = y + board.block_height + padding_h + plus_y
        elif pos == 2:
            pos_x = x + padding_w + plus_x
            pos_y = y + board.block_height - text.get_height() + plus_y
        elif pos == 3:
            pos_x = x + board.block_width - text.get_width() - padding_w + plus_x
            pos_y = y + board.block_height - text.get_height() + plus_y
        elif pos == 4:
            pos_x = x + board.block_width - text.get_width() - padding_w + plus_x
            pos_y = y + padding_h + plus_y
        else:
            raise Exception('Text position {} not allowed'.format(str(pos)))
        board.screen.blit(
            text, (pos_x, pos_y))

    def erase(self, board):
        if not board.visual:
            return
        blank_space = 2
        x, y = self.coordinates(board)
        size = int((board.block_width - blank_space*2)*self.size/100)
        content = pygame.Rect(
            [x + (board.block_width-size)/2, y + (board.block_height-size)/2, size, size])
        pygame.draw.rect(board.screen, board.FLOOR, content)
        pygame.display.update()

    def debug(self):
        return str(self.__class__) + ' | ' + str(self)

    def __str__(self):
        return 'pos: ' + str(self.pos)

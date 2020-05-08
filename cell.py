import pygame
# from board import Board
from content import Content


class Cell:

    WHITE = (100, 100, 100)

    def __init__(self, pos: int, x: int, y: int, content: Content = None):
        self.pos = pos
        self.x = x
        self.y = y
        self.content = content

    def empty(self):
        return not isinstance(self.content, Content)

    def content(self):
        return self.content

    def occupy(self, content: Content):
        if not self.empty:
            raise Exception('Cell already occupied')
        self.content = content

    def come_in(self, cell_from):
        content = cell_from.leave()
        self.content = content

    def leave(self):
        content = self.content
        self.content = None
        return content

    def draw(self, board):
        # Print cell terrain
        # x, y = self.x * board.block_width, self.y * board.block_height
        # # print('('+str(x)+','+str(y)+')' + '['+str(x+1)+','+str(y+1)+', '+str(board.block_width-1)+', '+str(board.block_height-1)+']')
        # cell = pygame.Rect(
        #     [x+1, y+1, board.block_width-1, board.block_height-1])
        # pygame.draw.rect(board.screen, self.WHITE, cell)

        if not self.empty():
            self.content.draw(board)
            # self.content.draw_debug_text(board, some_text)

    def debug(self):
        print('Cell | pos: ' + str(self.pos) + ' | x: ' + str(self.x) + ' | y: ' + str(self.y) + ' | ' +
              (' empty' if self.empty() else ' => ' + str(self.content)))

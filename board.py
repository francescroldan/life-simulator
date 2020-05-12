import pygame
import copy
import numpy as np
from cell import Cell
from colors import Colors


class Board:

    FLOOR = Colors.WHITE.value
    GRID = Colors.BLACK.value

    def __init__(self, cols: int, rows: int, block_width: int, block_height: int, visual: bool = True):
        self.visual = visual
        self.cols = cols
        self.rows = rows
        self.margin_vertical = 50  # margin_vertical
        self.margin_horizontal = 50  # margin_horizontal
        self.block_width = block_width
        self.block_height = block_height
        self.size = (cols * block_width, rows * block_height)
        self.screen = pygame.display.set_mode(
            self.size, 0, 24)  # New 24-bit screen
        self.cells = {}
        self.create_grid()

    def create_grid(self):
        for x in range(self.cols):
            for y in range(self.rows):
                pos = x * self.cols + y
                # print('Printing('+str(pos)+') x: ' + str(x) + '  y: ' + str(y))
                self.cells[pos] = Cell(pos, x, y)

    def draw_grid(self):
        if not self.visual:
            return
        for i in range(self.cols):
            start_point = (i * self.block_width, 0)
            end_point = (i * self.block_width, self.size[1])
            # print("(" + str(start_point) + ', ' + str(end_point) + ")")
            pygame.draw.line(self.screen, self.GRID,
                             start_point, end_point, 1)
        for i in range(self.rows):
            start_point = (0, i * self.block_height)
            end_point = (self.size[0], i * self.block_height)
            pygame.draw.line(self.screen, self.GRID,
                             start_point, end_point, 1)

    def empty_cells(self):
        cells = []
        for pos in self.cells:
            if self.cells[pos].empty():
                cells.append(self.cells[pos])
        return cells

    def filled_cells(self):
        cells = []
        for pos in self.cells:
            if not self.cells[pos].empty():
                cells.append(self.cells[pos])
        return cells

    def draw_cells(self):
        for pos in self.cells:
            self.cells[pos].draw(self)
        pygame.display.update()

    def cell(self, pos: int):
        return self.cells[pos]

    def cell_by_coords(self, x: int, y: int):
        return self.cells[x * self.cols + y]

    def copy_cells(self):
        return copy.deepcopy(self.cells)

    def adjacent_positions(self, pos: int, distance: int):
        matrix = []
        for width in range(0, 2*distance+1):
            line = []
            for y in range(pos - (self.cols*(distance-width))-distance, pos - (self.cols*(distance-width)) +
                           distance+1):
                if y >= 0 and y < len(self.cells) and y != pos:
                    line.append(y)
            matrix += line
        return matrix

    def adjacent_cells(self, pos: int, dist: int):
        adjacent_cells = []
        # self.printAdjacentCells(pos, dist)
        for cell_pos in self.adjacent_positions(pos, dist):
            # print('pos_found: ' + str(cell_pos))
            cell = self.cell(cell_pos)
            if cell_pos != pos:
                adjacent_cells.append(cell)
        return adjacent_cells

    def printAdjacentCells(self, pos: int, dist: int):
        print('adjacent positions: ')
        print(self.adjacent_positions(pos, dist))

    def erase(self):
        if not self.visual:
            return
        self.screen.fill(self.FLOOR)

    def debug(self):
        print('Debugging cells')
        for pos in list(self.cells):
            self.cells[pos].debug()

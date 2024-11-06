from time import sleep
from cell import Cell
from graphics import Point


class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self._create_cells()

    def _create_cells(self):
        self._cells = []
        for col in range(self.num_cols):
            column = []
            for row in range(self.num_rows):
                cell = Cell(True, True, True, True,
                            self.x1 + (col * self.cell_size_x),
                            self.x1 + ((col + 1) * self.cell_size_x),
                            self.y1 + (row * self.cell_size_y),
                            self.y1 + ((row + 1) * self.cell_size_y),
                            self.win)
                column.append(cell)

            self._cells.append(column)

        for col in range(self.num_cols):
            for row in range(self.num_rows):
                self._draw_cell(col, row)
                self._animate()

    def _draw_cell(self, i, j):
        cell = self._cells[i][j]
        cell.draw(Point(cell._x1, cell._y1), Point(cell._x2, cell._y2))

    def _animate(self):
        self.win.redraw()
        sleep(0.05)

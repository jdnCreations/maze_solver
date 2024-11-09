from operator import pos
import random
from time import sleep
from cell import Cell
from graphics import Point


class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None):
        if type(num_rows) != int or type(num_cols) != int:
            raise ValueError("Number of rows and columns must be integers.")
        if num_rows <= 0 or num_cols <= 0:
            raise ValueError(
                "Number of rows and columns must be greater than 0.")
        self._cells = []
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        if seed:
            random.seed(seed)
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()

    def _create_cells(self):
        for i in range(self._num_cols):
            col_cells = []
            for j in range(self._num_rows):
                cell = Cell(self._win)
                col_cells.append(cell)
            self._cells.append(col_cells)

        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        if self._win is None:
            return
        x1 = self._x1 + i * self._cell_size_x
        y1 = self._y1 + j * self._cell_size_y
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2)
        # self._animate()

    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        sleep(0.05)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        self._cells[self._num_cols - 1][self._num_rows -
                                        1].has_bottom_wall = False
        self._draw_cell(self._num_cols - 1, self._num_rows - 1)

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            possible_directions = []
            # left
            if i > 0 and not self._cells[i-1][j].visited:
                possible_directions.append((i-1, j))
            # right
            if i < self._num_cols - 1 and not self._cells[i+1][j].visited:
                possible_directions.append((i+1, j))
            # up
            if j > 0 and not self._cells[i][j-1].visited:
                possible_directions.append((i, j-1))
            # down
            if j < self._num_rows - 1 and not self._cells[i][j+1].visited:
                possible_directions.append((i, j+1))

            if len(possible_directions) == 0:
                self._draw_cell(i, j)
                return

            direction_index = random.randrange(len(possible_directions))
            next_index = possible_directions[direction_index]
            if next_index[0] == i + 1:
                self._cells[i][j].has_right_wall = False
                self._cells[i+1][j].has_left_wall = False
            if next_index[0] == i - 1:
                self._cells[i][j].has_left_wall = False
                self._cells[i-1][j].has_right_wall = False
            if next_index[1] == j + 1:
                self._cells[i][j].has_bottom_wall = False
                self._cells[i][j+1].has_top_wall = False
            if next_index[1] == j - 1:
                self._cells[i][j].has_top_wall = False
                self._cells[i][j-1].has_bottom_wall = False

            self._break_walls_r(next_index[0], next_index[1])

    def _reset_cells_visited(self):
        for row in self._cells:
            for cell in row:
                cell.visited = False

    def solve(self):
        return self._solve_r(0, 0)

    def _solve_r(self, i, j):
        self._animate()
        self._cells[i][j].visited = True
        if self._cells[i][j] == self._cells[-1][-1]:
            return True
        # up
        if j > 0:
            if self._cells[i][j-1] is not None and not self._cells[i][j-1].visited and not self._cells[i][j].has_top_wall:
                self._cells[i][j].draw_move(self._cells[i][j-1])
                result = self._solve_r(i, j-1)
                if result:
                    return True
                self._cells[i][j-1].draw_move(self._cells[i][j])

        # down
        if j < len(self._cells[0]) - 1:
            if self._cells[i][j+1] is not None and not self._cells[i][j+1].visited and not self._cells[i][j].has_bottom_wall:
                self._cells[i][j].draw_move(self._cells[i][j+1])
                result = self._solve_r(i, j+1)
                if result:
                    return True
                self._cells[i][j+1].draw_move(self._cells[i][j])

        # right
        if i < len(self._cells) - 1:
            if self._cells[i+1][j] is not None and not self._cells[i+1][j].visited and not self._cells[i][j].has_right_wall:
                self._cells[i][j].draw_move(self._cells[i+1][j])
                result = self._solve_r(i+1, j)
                if result:
                    return True
                self._cells[i+1][j].draw_move(self._cells[i][j])

        # left
        if i > 0:
            if self._cells[i-1][j] is not None and not self._cells[i-1][j].visited and not self._cells[i][j].has_left_wall:
                self._cells[i][j].draw_move(self._cells[i-1][j])
                result = self._solve_r(i-1, j)
                if result:
                    return True
                self._cells[i-1][j].draw_move(self._cells[i][j])

        return False

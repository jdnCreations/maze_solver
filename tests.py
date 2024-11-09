from multiprocessing import Value
import unittest

from graphics import Window
from maze import Maze


class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_maze_create_min(self):
        num_rows = 1
        num_cols = 1
        m1 = Maze(0, 0, num_rows, num_cols, 1, 1)
        self.assertEqual(len(m1._cells), num_cols)
        self.assertEqual(len(m1._cells[0]), num_rows)

    def test_maze_no_cells(self):
        num_rows = 0
        num_cols = 0
        with self.assertRaises(ValueError, msg="Number of rows and columns must be greater than 0."):
            Maze(0, 0, num_rows, num_cols, 0, 0)

    def test_maze_negative(self):
        num_rows = -5
        num_cols = -8
        with self.assertRaises(ValueError, msg="Number of rows and columns must be greater than 0."):
            Maze(0, 0, num_rows, num_cols, 0, 0)

    def test_maze_non_integer(self):
        num_rows = "f"
        num_cols = 2
        with self.assertRaises(ValueError, msg="Number of rows and columns must be integers."):
            Maze(0, 0, num_rows, num_cols, 0, 0)

    def test_maze_break_entrance_exit(self):
        num_rows = 2
        num_cols = 2
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(m1._cells[0][0].has_top_wall, False)
        self.assertEqual(m1._cells[-1][-1].has_bottom_wall, False)

    def test_maze_reset_cells_visited(self):
        m1 = Maze(0, 0, 20, 20, 10, 10, None, 5)

        for row in m1._cells:
            for cell in row:
                self.assertEqual(cell.visited, False)


if __name__ == "__main__":
    unittest.main()

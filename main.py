from tkinter import Tk, BOTH, Canvas

from cell import Cell
from graphics import Line, Point, Window
from maze import Maze


def main():
    window = Window(600, 400)

    maze = Maze(5, 5, 5, 5, 5, 5, window)

    p1 = Point(20, 200)
    p2 = Point(40, 350)
    line = Line(p1, p2)
    window.draw_line(line, "red")

    all_walls_cell = Cell(_x1=50, _x2=100, _y1=50, _y2=100, _win=window)
    all_walls_cell.draw(Point(50, 50), Point(100, 100))

    left_wall_cell = Cell(True, False, False, False, 60, 110, 100, 150, window)
    left_wall_cell.draw(Point(60, 110), Point(100, 150))

    all_walls_cell.draw_move(left_wall_cell)

    window.wait_for_close()


main()

from tkinter import Tk, BOTH, Canvas

from cell import Cell
from graphics import Line, Point, Window
from maze import Maze


def main():
    width = 1920
    height = 1080
    window = Window(width, height)

    rows = 10
    cols = 10
    cell_size_x = width / rows
    cell_size_y = height / cols

    maze = Maze(5, 5, rows, cols, cell_size_x, cell_size_y, window, 10)

    maze.solve()
    window.wait_for_close()


main()

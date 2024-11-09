from tkinter import Tk, BOTH, Canvas

from cell import Cell
from graphics import Line, Point, Window
from maze import Maze


def main():
    window = Window(800, 600)

    maze = Maze(5, 5, 5, 5, 50, 50, window, 5)
    window.wait_for_close()


main()

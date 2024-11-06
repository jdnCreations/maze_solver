

from tkinter import W
from graphics import Line, Point, Window


class Cell:
    def __init__(self, has_left_wall=True, has_right_wall=True, has_top_wall=True, has_bottom_wall=True, _x1=None, _x2=None, _y1=None, _y2=None, _win: Window = None):
        self.has_left_wall = has_left_wall
        self.has_right_wall = has_right_wall
        self.has_top_wall = has_top_wall
        self.has_bottom_wall = has_bottom_wall
        self._x1 = _x1
        self._x2 = _x2
        self._y1 = _y1
        self._y2 = _y2
        self._win = _win

    def draw(self, top_left_corner: Point, bottom_right_corner: Point):
        if self.has_left_wall:
            line = Line(top_left_corner, Point(
                top_left_corner.x, bottom_right_corner.y))
            self._win.draw_line(line, "red")
        if self.has_right_wall:
            line = Line(Point(bottom_right_corner.x,
                        top_left_corner.y), bottom_right_corner)
            self._win.draw_line(line, "blue")
        if self.has_top_wall:
            line = Line(top_left_corner, Point(
                bottom_right_corner.x, top_left_corner.y))
            self._win.draw_line(line, "orange")
        if self.has_bottom_wall:
            line = Line(Point(top_left_corner.x,
                        bottom_right_corner.y), bottom_right_corner)
            self._win.draw_line(line, "green")

    def draw_move(self, to_cell, undo=False):
        color = "red"
        if undo:
            color = "gray"

        # current cell center
        current = Point((self._x1 + self._x2) / 2, (self._y1 + self._y2) / 2)
        to = Point((to_cell._x1 + to_cell._x2) / 2,
                   (to_cell._y1 + to_cell._y2) / 2)
        self._win.draw_line(Line(current, to), color)

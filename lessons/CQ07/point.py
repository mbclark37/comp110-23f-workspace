"""Defining a point class."""

from __future__ import annotations


class Point:
    """Point class."""
    x: float
    y: float

    def __init__(self, x_init: float, y_init: float):
        """Constructor."""
        self.x = x_init
        self.y = y_init
    
    def scale_by(self, factor: int) -> None:
        """Scales the original point by a certain factor."""
        self.x *= factor
        self.y *= factor

    def scale(self, factor: int) -> Point:
        """Creates a new point based off of the scale factor."""
        new_point: Point = Point(self.x * factor, self.y * factor)
        return new_point
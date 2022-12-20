import math
from abc import ABC

from steps.src.command import Command
from steps.src.move import Movable


class Rotable(ABC):

    def get_direction(self):
        pass

    def get_angular_velocity(self):
        pass

    def set_direction(self, new_value):
        pass

    def get_directions_number(self):
        pass


class Rotate:
    def __init__(self, r: Rotable):
        self.r = r

    def execute(self):
        self.r.set_direction(self.r.get_direction() +
                             self.r.get_angular_velocity() %
                             self.r.get_directions_number())


class ChangeVelocityCommand(Command):
    def __init__(self, m: Movable, r: Rotable):
        self.m = m
        self.r = r

    def execute(self):
        x_coord = 0
        y_coord = 1
        x = self.m.get_position()[x_coord] * math.cos(
            2 * math.pi * self.r.get_direction()
            / self.r.get_directions_number()) \
            + self.m.get_position()[y_coord] * math.sin(
            2 * math.pi * self.r.get_direction()
            / self.r.get_directions_number())

        y = self.m.get_position()[y_coord] * math.cos(
            2 * math.pi * self.r.get_direction()
            / self.r.get_directions_number()) \
            + self.m.get_position()[x_coord] * math.sin(
            2 * math.pi * self.r.get_direction()
            / self.r.get_directions_number())
        x = int(round(x))
        y = int(round(y))
        self.m.set_position([int(x), int(y)])

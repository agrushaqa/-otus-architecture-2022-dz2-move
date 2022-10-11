from abc import ABC


class Movable(ABC):
    def get_position(self):
        pass

    def get_velocity(self):
        pass

    def set_position(self, new_value):
        pass

    def add(self, x, y):
        pass


class Move:
    def __init__(self, m: Movable):
        self.m = m

    def execute(self):
        self.m.set_position(self.m.add(self.m.get_position(), self.m.get_velocity()))

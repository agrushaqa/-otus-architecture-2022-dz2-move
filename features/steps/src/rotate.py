from abc import ABC


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

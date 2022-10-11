# before every scenario
from unittest.mock import MagicMock

import numpy as np
from steps.src.move import Movable


class MockPosition:
    def __init__(self):
        self.coord = None

    def get_position(self):
        return self.coord

    def set_position(self, new_value):
        self.coord = new_value


def mock_add(x, y):
    return np.add(x, y).tolist()


def before_feature(context, feature):
    mock_position = MockPosition()
    context.mock = MagicMock(spec=Movable)
    context.mock.add = mock_add
    context.mock.set_position = mock_position.set_position
    context.mock.get_position = mock_position.get_position

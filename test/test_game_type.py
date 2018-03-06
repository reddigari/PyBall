import pytest
from PyBall import PyBall
from models.game_types import GameType

from exceptions import *

@pytest.fixture(scope='module')
def test_game_type():
    pyball = PyBall()
    return pyball.get_game_types()


def test_get_game_types_returns_list_of_game_types(test_game_type):
    assert isinstance(test_game_type, list)
    assert isinstance(test_game_type[0], GameType)
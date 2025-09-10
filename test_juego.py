import pytest
from unittest.mock import patch
import builtins
import random


from script import startGame, gen_random_number

def test_gen_random_number_range():
    """Verifica que el número generado esté dentro del rango dado"""
    for _ in range(50):
        num = gen_random_number(1, 10)
        assert 1 <= num <= 10


def test_startGame_loses(capsys):
    """Prueba cuando el usuario NO adivina el número"""
    with patch.object(builtins, "input", lambda: "3"), \
         patch.object(random, "randint", lambda a, b: 7):
        startGame()

    captured = capsys.readouterr()
    assert "sorry you didnt get it" in captured.out
    assert "the number was 7" in captured.out

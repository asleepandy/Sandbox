from main.example import example1, example2
import pytest


def test_example1():
    # print example1(10)
    assert example1(10) == -4


def test_example2():
    assert example2(100, 5) == 5

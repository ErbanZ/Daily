# coding=utf-8

# Description: The file description here

import pytest
import os
import sys

LIB_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
if LIB_PATH not in sys.path:
    sys.path.append(LIB_PATH)

from Common.Calculator import Calculator


class Test_Calculator:
    def test_add1(self, info_start):
        calc = Calculator()
        result = calc.add(2, 3)
        assert result == 5

    def test_add2(self):
        calc = Calculator()
        result = calc.add(2, 3)
        assert result == 4

    def test_subtract1(self):
        calc = Calculator()
        result = calc.subtract(5, 3)
        assert result == 2

    def test_subtract2(self):
        calc = Calculator()
        result = calc.subtract(5, 3)
        assert result == 1


if __name__ == '__main__':
    pass

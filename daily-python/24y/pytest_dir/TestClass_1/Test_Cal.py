# coding=utf-8

# Description: The file description here

import pytest


@pytest.fixture()
def info_start():
    print('TEST START')


@pytest.fixture()
def info_end():
    print('TEST END')


def add(a, b):
    return a + b


def test_add1(info_start):
    result = add(2, 3)
    assert result == 5


if __name__ == '__main__':
    pass

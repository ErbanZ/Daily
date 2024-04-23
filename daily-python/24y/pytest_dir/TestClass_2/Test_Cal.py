# coding=utf-8

# Description: The file description here


def add(a, b):
    return a + b


def test_add1(tip_info_module):
    result = add(2, 3)
    assert result == 5


def test_add2():
    result = add(2, 3)
    assert result == 5


if __name__ == '__main__':
    pass

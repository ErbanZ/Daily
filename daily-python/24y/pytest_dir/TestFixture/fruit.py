# coding=utf-8

# Description: The file description here

import pytest


class Fruit:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return self.name == other.name


@pytest.fixture
def my_fruit():
    # 这里是一个fixture，返回了一个Fruit对象，名字叫苹果
    return Fruit("苹果")


@pytest.fixture
def fruit_basket(my_fruit):
    # 这里是另一个fixture，同样声明一个Fruit对象，名字叫香蕉。
    # 然后在这个fixture中又传入了上一个fixture：my_fruit
    # 最后把最终的返回装到一个列表[]里，返回
    return [Fruit("香蕉"), my_fruit]


def test_my_fruit_in_basket(my_fruit, fruit_basket):
    # 这是一个测试函数，可以使用多个fixture
    assert my_fruit in fruit_basket


if __name__ == '__main__':
    pass

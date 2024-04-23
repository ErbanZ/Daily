# coding=utf-8

# Description: The file description here

import pytest


@pytest.fixture(params=['参数1', '参数2'])
def my_fixture(request):
    print('\nmy_fixture')
    return request.param


def test_fixtures_01(my_fixture):
    print('\n执行test_fixtures_01')
    print(my_fixture)


def test_fixtures_02(my_fixture):
    print('\n执行test_fixtures_02')
    print(my_fixture)


if __name__ == '__main__':
    pass

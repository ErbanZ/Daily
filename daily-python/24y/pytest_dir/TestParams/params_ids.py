# coding=utf-8

# Description: The file description here


import pytest


@pytest.fixture(params=['参数1', '参数2'], ids=["id-01", "id-02"])
def my_fixture(request):
    return request.param


def test_fixtures_01(my_fixture):
    print('\n 执行test_fixtures_01')
    print(my_fixture)


if __name__ == '__main__':
    pass

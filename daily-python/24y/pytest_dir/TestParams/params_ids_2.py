# coding=utf-8

# Description: The file description here


import pytest


def init_data(fixture_value):
    if fixture_value == 1:
        return "unsold"
    elif fixture_value == 2:
        return "onSale"
    elif fixture_value == 3:
        return "sellOut"


@pytest.fixture(params=[1, 2, 3], ids=init_data)
def my_method(request):
    req_param = request.param
    print("\n参数为：【{}】,执行sql--插入【{}】状态的数据".format(req_param, req_param))
    yield req_param
    print("\n执行sql--清理参数为【{}】的测试数据".format(req_param, req_param))
    print("\n----------------------------------------")


def test_method_01(my_method):
    print("\n正在执行【{}】的case--".format(my_method))


if __name__ == '__main__':
    pass

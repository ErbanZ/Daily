# coding=utf-8

"""
Description: 自定义fixture夹具，若要全局使用需要在项目根目录添加文件pytest.ini
参考链接: https://blog.csdn.net/weixin_42023035/article/details/132769168
"""

import pytest


@pytest.fixture()
def tip_info_default():
    print('\nTEST START in TestClass_2')
    yield
    print('\nTEST END in TestClass_2')


@pytest.fixture(scope='function')
def tip_info_function():
    print('\nTEST START in TestClass_2')
    yield
    print('\nTEST END in TestClass_2')


@pytest.fixture(scope='class')
def tip_info_class():
    print('\nTEST START in TestClass_2')
    yield
    print('\nTEST END in TestClass_2')


@pytest.fixture(scope='module')
def tip_info_module():
    print('\nTEST START in TestClass_2')
    yield
    print('\nTEST END in TestClass_2')


@pytest.fixture(scope='session')
def tip_info_session():
    print('\nTEST START in TestClass_2')
    yield
    print('\nTEST END in TestClass_2')


if __name__ == '__main__':
    pass

# coding=utf-8

"""
Description: 自定义fixture夹具，若要全局使用需要在项目根目录添加文件pytest.ini
参考链接: https://blog.csdn.net/weixin_42023035/article/details/132769168
参考链接: https://blog.csdn.net/qq_45731111/article/details/107839185
"""

import pytest


@pytest.fixture()
def info_start():
    print('TEST START in conftest')


@pytest.fixture()
def info_end():
    print('TEST END')


if __name__ == '__main__':
    pass

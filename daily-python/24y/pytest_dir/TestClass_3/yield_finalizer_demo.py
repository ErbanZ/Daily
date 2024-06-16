# coding=utf-8

# Description: The file description here

# yield_finalizer_demo.py

import pytest


@pytest.fixture()
def demo_fixture1():
    print("\n这个fixture在每个case前执行一次")
    yield
    print("\n在每个case完成后执行的teardown")


def test_01(demo_fixture1):
    print("===执行了case: test_01===")


def test_02(demo_fixture1):
    print("===执行了case: test_02===")


def test_03(demo_fixture1):
    print("===执行了case: test_03===")


@pytest.fixture()
def demo_fixture2(request):
    print("\n这个fixture在每个case前执行一次")

    def demo_finalizer():
        print("\n在每个case完成后执行的teardown")

    def demo_finalizer2():
        print("\n在每个case完成后执行的teardown2")

    def demo_finalizer3():
        print("在每个case完成后执行的teardown3")

    # 注册demo_finalizer为终结函数，可以注册多个
    request.addfinalizer(demo_finalizer)
    request.addfinalizer(demo_finalizer2)
    request.addfinalizer(demo_finalizer3)


def test_11(demo_fixture2):
    print("\n===执行了case: test_11===")


def test_12(demo_fixture2):
    print("\n===执行了case: test_12===")


def test_13(demo_fixture2):
    print("\n===执行了case: test_13===")


@pytest.fixture()
def demo_fixture3():
    for i in [2, 0, 1]:
        print('i:', i)
        n = 10 / i
        yield
        print('res:', n)


@pytest.fixture()
def demo_fixture4(request):
    for i in [2, 0, 1]:
        print('i:', i)
        n = 10 / i
        request.addfinalizer(print('res:', n))


def test_23(demo_fixture1):
    print("\n===执行了case: test_13===")


if __name__ == '__main__':
    pass

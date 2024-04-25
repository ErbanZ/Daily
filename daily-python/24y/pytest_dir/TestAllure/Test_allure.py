# coding=utf-8

# Description: The file description here

import allure
import pytest
import os


@allure.feature('test_success')
def test_success():
    """this test succeeds"""
    assert True


@allure.feature('test_failure')
def test_failure():
    """this test fails"""
    assert False


@allure.feature('test_skip')
def test_skip():
    """this test is skipped"""
    pytest.skip('for a reason!')


@allure.feature('test_broken')
def test_broken():
    raise Exception('oops')


@allure.feature("用户管理")
@allure.story("用户登录")
class TestUserLogin:
    @allure.title("成功的登录")
    def test_user_login_success(self):
        # 测试逻辑
        assert True

    @allure.title("失败的登录")
    @allure.step("输入用户名")
    @allure.step("输入密码")
    @allure.step("提交登录")
    def test_user_login_failure(self):
        # 测试逻辑
        assert False


if __name__ == '__main__':
    # pytest.main(["-s","allure-test.py"])
    '''
    -q: 安静模式, 不输出环境信息
    -v: 丰富信息模式, 输出更详细的用例执行信息
    -s: 显示程序中的print/logging输出
    '''
    pytest.main(['-s', '-q', f'{__file__}', '--clean-alluredir', '--alluredir=allure-results'])
    os.system(r"allure generate -c allure-results -o allure-report")

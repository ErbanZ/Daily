# coding=utf-8

# Description: The file description here
import threading
import time
import os
from func_timeout import func_timeout, FunctionTimedOut


def my_test(name):
    print('子进程运行中，name={}，pid={}'.format(name, os.getpid()))
    time.sleep(40)
    print('子进程已经结束')


if __name__ == '__main__':
    print('父进程：{}'.format(os.getpid()))
    try:
        func_timeout(5, my_test, args=('test', ))
    except FunctionTimedOut as e:
        print(f'子程序超时:\n{e}')


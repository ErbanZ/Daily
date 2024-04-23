# coding=utf-8

# Description: The file description here
import threading
import time
import os
from func_timeout import func_set_timeout


@func_set_timeout(5)
def my_test(name):
    print('子进程运行中，name={}，pid={}'.format(name, os.getpid()))
    time.sleep(41)
    print('子进程已经结束')


if __name__ == '__main__':
    print('父进程：{}'.format(os.getpid()))
    try:
        p = threading.Thread(target=my_test, args=('test',))
        p.start()
        print('父进程：{}'.format(os.getpid()))
        print('父进程：{}'.format(os.getpid()))
    except TimeoutError as e:
        print('子程序超时')


# coding=utf-8

# Description: The file description here


def demo_decorator(func):
    def wrapper(*args, **kwargs):
        print('demo_decorator')
        func(*args, **kwargs)

    return wrapper


@demo_decorator
def demo(a, b):
    print(a + b)


if __name__ == '__main__':
    pass

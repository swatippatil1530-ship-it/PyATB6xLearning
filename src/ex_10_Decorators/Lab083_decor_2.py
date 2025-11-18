import time


def decoratoe_1(func):
    def wrapper():
        print("Decorator 1")
        func()
    return wrapper

def decoratoe_2(func):
    def wrapper():
        print("Decorator 2")
        func()
    return wrapper
@decoratoe_2
@decoratoe_1
def say_hello():
    print("Hello")
say_hello()
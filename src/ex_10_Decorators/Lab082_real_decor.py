import time

def print_logs(func):
    def wrapper():
        print("start of logging")
        func()
        print("end of logging")
    return wrapper

def time_decorator(func):
    def wrapper():
        start_time = time.time()
        print("start_time")
        func()
        end_time = time.time()
        print("end_time")
    return wrapper

@time_decorator
@print_logs
def test_UI_1():
    print("Add a function,time taken by this function")
    time.sleep(2)

@time_decorator
@print_logs
def test_UI_2():
    print("Add a function,time taken by this function")
    time.sleep(2)

test_UI_1()
test_UI_2()
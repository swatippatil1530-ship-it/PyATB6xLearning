def before_after_ui_test(func):

    def wrapper():
        print("before running UI code")
        func()
        print("after running UI code")
    return wrapper()

@before_after_ui_test
def test_UI():
    print("iam testing UI test")
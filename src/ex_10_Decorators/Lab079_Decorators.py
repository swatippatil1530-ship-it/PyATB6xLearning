
def add_security(func):

    def wrapper():
        print("1.before the function is called")
        print("2.add helmet,gloves,license,dashcash")
        func()
        print("3.after the function is called")
        print("4.secure driving, leave all the time")
    return wrapper()


@add_security
def drive_ola_scooter():
    print("iam driving ola scooter")


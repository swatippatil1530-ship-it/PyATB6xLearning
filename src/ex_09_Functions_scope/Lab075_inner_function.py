def outer_function():
    var1 = 30 #local

    def inner_function():
        var2 = 30
        print(var1)

    def inner_function2():
        var3 = 40
        print(var3)

    inner_function()
    inner_function2()

outer_function()
#inner_function()
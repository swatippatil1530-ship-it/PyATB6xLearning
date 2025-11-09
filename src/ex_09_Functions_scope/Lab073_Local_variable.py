pg_global = 12   #globle variable

def my_function():
    pg_a = 10   #local variable
    print(pg_a)
    print(pg_global)  #globle variable

#print(pg_a)  #local variable
print(pg_global)
my_function()

#local variable we can use inside the function it will give error outside the function
#global variable will use both inside and outside the function its global

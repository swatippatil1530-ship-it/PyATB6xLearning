#user defined
#1.they can't return ->non return
#2.they can return something
#3.they have parameter
#4.they dont have parametr/ argumentes

import math

#built in function
result = max(3, 4)
print(result)


#1.they can't return ->non return
def greet():
    print("Hello")


#2.they can't return type and parameter/argumentes
def greet_by_name(name):
    print("Hello", name)


greet_by_name("shreyas")


#3.they can't return type with default argumentes

def greet_by_name(name="swag"):
    print("Hello", name.title())


greet_by_name("swati")
greet_by_name()

#
def multiple_argu(name1="a", name2="b"):
    print("Hello", name1, name2)

multiple_argu()
multiple_argu("shreyas", "shreyas")
multiple_argu(name1="swati", name2="patil")
multiple_argu(name1="swati")
multiple_argu(name2="patil")
multiple_argu(name1="patil", name2="swati")


#4.they can return something they have parameter

def sum_of_two_numbers(number1=100, number2=20):
    return number1 + number2

result = sum_of_two_numbers(3, 4)
print(result)

result = sum_of_two_numbers(number1=100, number2=30)
print(result)

result = sum_of_two_numbers()
print(result)
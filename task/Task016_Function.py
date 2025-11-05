"""Q - Create a function which will take a positive number
 from the user and perform square of the number?

i/o = 3

o/p = 9
"""

def square(num):
    if num>0:
         print(num ** 2)
    else:
        print("enter a positive number")
square(int(input("enter a positive number:")))
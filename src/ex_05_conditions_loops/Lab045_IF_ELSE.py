#problem to find the max between two number.
#logic building formula
#step1: user i/p --two integer or float
#s2: o/p---int means 1 which is greater it will return
#s3  : 3.5 or 2.5 -- float

num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))

#if num1 > 0 and num2 >0:
#    print("number should be positive")

if num1 > num2:
    print("maximum", num1)
else:
    print("maximum" , num2)

#edge case : both are equal num1 = num2
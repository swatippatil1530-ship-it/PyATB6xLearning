#problem find the max b/w 3 numbers

#logic building
#user input num 1,num2,num3 >int
#o/p -- int or string with mx num

num1 = int(input("Enter another number: "))  #5, #10
num2 = int(input("Enter another number: "))  #3, #12
num3 = int(input("Enter another number: "))  #2 ,#11

#num1>num2 and num1>num3--num1
#num2>num3 and num2>1num1--num2
#num3-max

if num1 >= num2 and num1 >= num3:
    print("maximum", num1)
elif num2 >= num3 and num2 >= num1:
    print("maximum", num2)
else:
    print("maximum", num3)

#creat a program to sum of three numbers from the user input
#if user doesn't enter any number,use default as 100,200,300

num1 = int(input("enter the num1: "))
num2 = int(input("enter the num2: "))
num3 = int(input("enter the num3: "))

#dont use the default argument name same as user input name try to diffrent
def sum_of_three_numbers(num1=100 , num2=200 , num3=300):
   return num1 + num2 + num3

"""result0 = sum_of_three_numbers(num1, num2, num3)
print(result0)
"""

def sum_of_three_numbers(n1=100 , n2=200 , n3=300):
   return n1 + n2 + n3

result = sum_of_three_numbers()  #using default parameter
print(result)

"""result2 = sum_of_three_numbers(num1=90)
print(result2)
"""
"""result3 = sum_of_three_numbers(num1=100 ,num2=200)
print(result3)
"""
#two value from default and on efrom user
result4 = sum_of_three_numbers(n1=20,n2=40, n3=num3)
print(result4)
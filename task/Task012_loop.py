"""Question 1.

Given a Number a number you need to calculate the factorial of that number
n = 5
Fact = 5×4×3*2*1 = 120
Fact = 0 → 1, """
from task.Task010_condition_loops import page_load_time

#num = 5
num = int(input("enter the number to get fact!: "))
fact = 1  # factorial start with 1

if num <=0:
    print("factorial = ",fact)
else:
    for i in range(1,num+1): #1,2,3,4,5
        fact = fact * i

print("factorial = ",fact)
#edge cases also need to cover

"""Question 2 : 

An API sometimes fails due to network delays.
Write a program to retry the API call 3 times until the response code becomes 200.

If it still fails after 3 tries, print a failure message.
Hint: Use a while loop with a counter.

Expected Output Example:
Attempt 1: Response 500
Attempt 2: Response 200
✅ Test Passed"""

attempt = 1
max_attempt = 3
response = None

while attempt <= max_attempt:
    response = int(input("enter the response code: "))
    if response == 200:
        print("Test Passed")
        break
    else:
        attempt = attempt + 1

if response != 200:
    print("Test Failed 3 attemptes tyr again letter")




"""Question 3 : 

Simulate a page loading check using a while loop.
If page_loaded becomes True within 5 seconds, print success; else timeout.

Hint: Use a counter (like wait_time) and break condition."""





#write a program to take a user age and
#let him know if he can go to the club
#age is greater than 21

#logic building formula
#step1:
#i/p - age(int)
#o/p - string(result-can go to club or not)

#step2: rough logic
# age > 21 -> he can go
# age < 21 -> he can't go

Age = int(input("enter the age : ").strip())  #strip() : remove the whitespace

if Age <=0 or Age > 130:
    print("enter a valid age")
else:
    if Age >= 21:
         print("yes, can go to club")
    else:
         print("no, can not go to club")

#step4:  check for the edge cases
#such as
#-ve ages or extremely high value -> program will break.
#non-numeric input--abc
#age which is valid >130

#step5:optimize the code
#handle all the edge
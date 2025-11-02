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

age = int(input("enter the age : "))
if age > 21:
    print("yes,can goto club")
else:
    print("no,can goto club")
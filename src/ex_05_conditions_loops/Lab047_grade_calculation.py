#grade calculation:
#write program that calculate and displays the letter grade
#for a given numerical score(ex: A,B,C,D,F)
#based on the following grading score

#A: 90-100
#B: 80-89
#C: 70-79
#D: 60-69
#F: 0-59

# logic building formula
#1 -> user input - score --int
#2 -> o/p str--> A,B,C

score = int(input("Enter a score: ").strip())
if score > 100 or score <=-1:
    print("score must be between 100 and -1")
else:
    if score >=90 and score <=100:
        print("your grade is A")
    elif score >=80 and score <=89:
        print("your grade is B")
    elif score >=70 and score <=79:
        print("your grade is C")
    elif score >=60 and score <=69:
        print("your grade is D")
    else:
       print("your grade is F")

#float,abc,try catch
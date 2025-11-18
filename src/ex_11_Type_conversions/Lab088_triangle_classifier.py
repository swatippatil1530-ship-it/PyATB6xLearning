#Triangle classifier

#write the program classifer of triangle

side1 = float(input("Enter side 1: "))
side2 = float(input("Enter side 2: "))
side3 = float(input("Enter side 3: "))

def triangle_classifier(side1, side2, side3):
    if side1>0 and side2>0 and side3>0:   #edge case
        if side1 + side2 > side3 and side1 + side3 > side2:    #edge case
            if side1 == side2 and side1 == side3 and side2 == side3:
                 print("equlatrel triangle")
            elif side1 == side2 and side2 == side3 and side3 != side1:
                print("isosceles triangle")
            else:
             print("scalene triangle")
        else:
            print("no valid length")
    else:
        print("no triangle")

triangle_classifier(side1, side2, side3)
"""Q - Create a function which will take the
 3 values from the user, which are length of the triangle.
   side1, side2, side2
i/p - int side1 == side2 =side3 → isoceles
o/p = result in string - iso, eq, scalene"""

def Traingle(side1, side2, side3):
    if side1 ==side2 ==side3:
        print("traingle is Equilater")

    elif side1 == side2 or side2 == side3 or side1 == side3:
        print("traingle is Isoceles")
    else:
        print("traingle is Scalene")
Traingle(int(input("enter side1: ")), int(input("enter side2: ")),int(input("enter side3: ")))
#write program to find the area of circle  using redius area = pi*radius^2
#i/o ---float
#o/p---string formatted type

#logical building formula

#step:1
#figure out the input and outputs
#input r data type>>>float
#pi = 3.14
# power > pow or **> any
#o/p>>>string > float-area, print ara
import math
#step 2:
#rough logic = area = 3.14 * (pow(r,2))

#step 3:
radius = float(input("enter the radius of the circle: "))
print("radius is",radius)
area_of_the_circle = math.pi * pow(radius, 2)
print(area_of_the_circle)
print(f"area of the circle is {area_of_the_circle:.2f}")

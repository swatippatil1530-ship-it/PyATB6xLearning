#find the positive number is even or odd

num = int(input("enter a number: ").strip())

if num >=0:
   if num % 2 == 0:
    print("even number")
   else:
    print("odd number")
else:
    print("negative number")

#you can write the code in short ternary operator
if num >= 0:
    print("even" if num % 2 == 0 else "odd")
else:
    print("Negative number")
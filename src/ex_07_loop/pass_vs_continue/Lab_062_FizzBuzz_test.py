#for multiple of 3 print fizz
#for multiple of 5 print buzz
#for multiple of both print fizzbuzz
#print number i


for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)

#fst we need to check for the both condition the go for single
#15 and 30 it will give error if you write last conditon as both
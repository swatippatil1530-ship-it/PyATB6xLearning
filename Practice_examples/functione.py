# Function Simulating a Dice Roll
import random
import string
from idlelib.colorizer import ColorDelegator


def roll_dice():
    return random.randint(1, 6)

print(roll_dice())


#is_vowel(letter)
# Returns True if the given character is a vowel, else False

def is_vowel(char):
    return char in 'aeiou'
char = input("enter a character: ")
vowel = is_vowel(char)
print(vowel)

#temperature_message(temp)
# Print "Cold", "Warm", or "Hot" based on the temperature.

def temperature_message(temp):
    match temp:
        case t if temp < 15:
            return "cold"
        case t if temp < 30:
            return "warm"
        case _ :
            return "Hot"

temp = int(input("enter a temperature: "))
temperature_message(temp)
print(temperature_message(temp))


#reverse_string(text)
# Returns the reverse of the given string.

def reverse_string(string):
    return string[::-1]
string = input("enter a string: ")
reverse_string(string)
print(reverse_string(string))

#is_palindrome(word)
# Returns True if the word reads the same forward and backward.

def is_polindrome(string):
    return string == string[::-1]
string = input("enter a string: ")
is_polindrome(string)
print(is_polindrome(string))
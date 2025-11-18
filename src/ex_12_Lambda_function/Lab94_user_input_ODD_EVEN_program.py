#write a program to calculate even and odd
"""def find_ODD_EVEN(n):
    if n % 2 == 0:
        return EVEN
    else:
        return ODD
        """


user_input = int(input("Enter the number : "))
check_even_odd = lambda num: "even" if num %2 == 0 else "odd"
print(check_even_odd(user_input))
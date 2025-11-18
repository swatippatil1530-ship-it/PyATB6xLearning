#check fpr a leap year->2024,yes

#lead day occurs in each year that is  a multiple of 4
#except the years evenly divisible bt 100 but not 400

#the year is multiple of 400
#te year is a multiple if 4 and not a multiple of 100

def check_leap_year(year):
    if (year % 4 == 0) and (year % 100!= 0) or (year % 400== 0):
        return True
    else:
        return False

year = 2024
#year = 2025
result = check_leap_year(year)
print(result)


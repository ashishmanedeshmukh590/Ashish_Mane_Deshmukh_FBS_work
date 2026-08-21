##10.WAP to check entered year is leap year or not. 

def IsLeapYear(year):

    return(year%4 == 0 and year % 100 !=0) or (year % 400 == 0)

year = int(input('Enter the year'))

if IsLeapYear(year):
    print(f'{year} is a leap year.')
else:
    print(f'{year} is not leap year.')
#Given a number, add its digits.
#e.g. given 29  then 2+9 =11 or 239 then return 2+3+9
#Python has a fast and easy solution. In other approaches, you can use / and % functions.
#convert to string, use list comprehension to make it a list of integers, use inbuilt sum() function

def addTwoDigits(n):
    digits=[int (x) for x in str(n)]
    return sum(digits)


# python number methods
# 1) rounding a number
# round() function rounds a floating point number to a specified decimal point
# syntax: round(number, ndigits)
# number -- the number to be rounded off
# ndigits -- the number of decimal places

pi = 3.1415926535897
two_decimals = round(pi, 2)
three_decimals = round(pi, 3)

print(two_decimals)
print(three_decimals)


# 2) raising a number to a power
# the pow() function is used to raise a number to a specified power
# syntax: pow(base, exp)
# base -- the base number 
# exp -- the exponent

x = pow(5, 2) # same as 5 * 5
y = pow(5, 3) # same as 5 * 5 * 5

print(x)
print(y)


# 3) getting absolute value
#  the abs() function returns the absolute value of a number
# in mathematics, the absolute value is the non-negative value of a number
# for example, the absolute value of 4 is 4 and the absolute value of -7 is 7

a = abs(-30)
b = abs(-2.75)

print(a)
print(b)


# 4) getting quotient and remainder
'''
the divmod() function takes two numbers and return a pair 
of numbers consisting of their quotient and remainder

in this example, 7 is divided by 2 therefore the 
quotient is 3 and the remainder is 1
'''

z = divmod(7, 2)
print(z)










